# -*- coding:utf-8 -*-

import logging
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
import aiomysql
from orm import Model, StringField, IntegerField


async def index(request):
    return web.Response(body=b'<h1>Home</h1>')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('Server started at http://127.0.0.1:9000')
    return srv

logging.basicConfig(level=logging.INFO)
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


# 创建数据库连接池
async def create_pool(loop, **kw):
    logging.info('create database connection pool....')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', '3306'),
        user=kw.get('user'),
        password=kw.get('password'),
        db=kw.get('db'),
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

async def select(sql, args, size=None):
    logging(sql, args)
    global __pool
    with await __pool as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs

async def execute(sql, args):
    logging.info(sql)
    with await __pool as conn:
        try:
            cur = await conn.cursor()
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount  # execute()和select()函数不同的是，cursor对象不返回结果集，通过rowcount返回结果数
            await cur.close()
        except BaseException as e:
            logging.warn(e)
            raise
        return affected

