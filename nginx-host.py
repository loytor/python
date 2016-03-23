#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @author:loytor@sina.com
# @date:2016-03-23

import os

if os.getenv("USER") != 'root' :
	print '------------------------------------------------------------------------'
	print '⚠️ 权限不足，需要root用户权限'
	print '------------------------------------------------------------------------'
	exit()
else :
    path = raw_input('请输入文件路径:')
    domain = raw_input('请输入域名：')
    
    if ( path == '' ) or ( domain == '' ) :
        print '文件路径和域名都不能为空'
        exit() 
    else :
        print '------------------------------------------------------------------------'
        print '⌛ 正在验证文件路径是否正常⌛'
        print '------------------------------------------------------------------------'
        if os.path.exists(path):
            print '路径正常⬇️ ----------------------------------------------------------'
        else:
            exit('⚠️ 文件路径不存在')
        print '------------------------------------------------------------------------'
        print '️当前路径是：' , path
        print '当前域名是：' , domain
        
        confirm = raw_input('确定使用当前域名创建虚拟主机吗？y/n：')
        if confirm == 'y' :
            
            full_path = '/usr/local/etc/nginx/servers/' + domain +'.conf'
            f = open(full_path,'w')
            f.close()
            
            f = file(full_path,"a+")
            txt = 'server {',"\n"
            txt += '    listen       80;',"\n"
            txt += '    server_name  ' + domain + ';',"\n"
            txt += '    root   '+ path +';',"\n"
            txt += '    location / {',"\n"
            txt += '        index index.php  index.html index.htm;',"\n"
            txt += '        if (!-f $request_filename){',"\n"
            txt += '            set $rule_0 1$rule_0;',"\n"
            txt += '        }',"\n"
            txt += '        if (!-d $request_filename){',"\n"
            txt += '            set $rule_0 2$rule_0;',"\n"
            txt += '        }',"\n"
            txt += '        if ($rule_0 = "21"){',"\n"
            txt += '            rewrite ^/(.*)$ /index.php?/$1 last;',"\n"
            txt += '        }',"\n"
            txt += '    }',"\n"
            txt += '    error_page   500 502 503 504  /50x.html;',"\n"
            txt += '    location = /50x.html {',"\n"
            txt += '        root   html;',"\n"
            txt += '    }',"\n"
            txt += '    location ~ \.php$ {',"\n"
            txt += '        fastcgi_pass   127.0.0.1:9000;',"\n"
            txt += '        fastcgi_index  index.php;',"\n"
            txt += '        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;',"\n"
            txt += '        include        fastcgi_params;',"\n"
            txt += '    }',"\n"
            txt += '}',"\n"
            
            f.writelines(txt)
            f.close()
            
            print domain , '.conf写入完成...'
            print '------------------------------------------------------------------------'
            f = file("/etc/hosts","a+")
            txt = '127.0.0.1	' + domain + "\n"
            f.writelines(txt)
            f.close()
            print 'host写入完成...'
            print '------------------------------------------------------------------------'
    
            reboot = raw_input('是否重启Nginx(y/n):')
            if reboot == 'y':
                os.system('nginx -s reload')
        else :
            exit('终止程序')