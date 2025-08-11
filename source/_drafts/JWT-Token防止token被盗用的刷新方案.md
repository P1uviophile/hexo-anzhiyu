---
title: 防止JWT的token被盗用后无限续杯的想?
author: Joking
tags:
  - JWT
categories:
  - 技术笔?
cover: 'https://pic.joking7.com/202407180210332.webp'
date: 2024-07-17 23:40:00
---



写一个refreshToken接口

1. refreshToken接口: 查询用户状态是否被冻结 如果被冻结则不返回新token 正常则返回新Token
2. 前端获取token过期的返回信息后调用refreshToken接口获取新token, 获取不到新token则返回登录界面并删除cookie中的token
3. 用户更改密码后将用户账号冻结一段时?即token的有效时? 同时在消息队列推送解封事?
