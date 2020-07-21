@load base/protocols/http/main.zeek
@load base/protocols/http/utils.zeek
@load base/frameworks/notice
@load base/frameworks/sumstats
@load base/protocols/http
export {
    redef enum Notice::Type += {
        attack_fpm,
    };
}

event tcp_packet(c: connection, is_orig: bool, flags: string, seq: count, ack: count, len: count, payload: string)
 {
if ( is_orig && "filemanager/sa/getZipFile?path=../" in payload || "filemanager/sa/getZipFile?path=/../" in payload  )
		if ( is_orig && "/var/www/html" in payload)
            {
            local n: Notice::Info = Notice::Info($note=attack_fpm, 
                                                 $msg="attack fpm ", 
                                                 $sub=payload,
                                                 $conn=c);
            NOTICE(n);
            }

 }
