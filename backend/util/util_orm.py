# -*- coding: utf-8 -*-

from tortoise.queryset import QuerySet

async def upsert(model, **kwargs):
    # 尝试根据提供的条件查询记录
    instance = await model.filter(**kwargs).first()

    # 如果记录存在，则更新它
    if instance:
        for key, value in kwargs.items():
            setattr(instance, key, value)
        await instance.save()
    # 如果记录不存在，则创建新记录
    else:
        instance = await model.create(**kwargs)

    return instance
