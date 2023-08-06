import sys ,os ,time ,io ,re ,traceback ,warnings ,weakref ,collections .abc ,random #line:1
from string import Template #line:3
from string import Formatter as StrFormatter #line:4
__all__ =['BASIC_FORMAT','BufferingFormatter','CRITICAL','DEBUG','ERROR','FATAL','FileHandler','Filter','Formatter','Handler','INFO','LogRecord','Logger','LoggerAdapter','NOTSET','NullHandler','StreamHandler','WARN','WARNING','addLevelName','basicConfig','captureWarnings','critical','debug','disable','error','exception','fatal','getLevelName','getLogger','getLoggerClass','info','log','makeLogRecord','setLoggerClass','shutdown','warn','warning','getLogRecordFactory','setLogRecordFactory','lastResort','raiseExceptions']#line:15
import threading #line:17
__author__ ="Vinay Sajip <vinay_sajip@red-dove.com>"#line:19
__status__ ="production"#line:20
__version__ ="0.5.1.2"#line:22
__date__ ="07 February 2010"#line:23
_OOOO0000OO00000O0 =time .time ()#line:32
raiseExceptions =True #line:38
OO0OOOO00OO0O0O0O =True #line:43
O00OO00OOO0O0O000 =True #line:48
O0O0OOOOO0OO00OOO =True #line:53
CRITICAL =50 #line:66
FATAL =CRITICAL #line:67
ERROR =40 #line:68
WARNING =30 #line:69
WARN =WARNING #line:70
INFO =20 #line:71
DEBUG =10 #line:72
NOTSET =0 #line:73
global OO000O0OOOO00O0OO #line:74
global OOO0O00000000OOO0 #line:75
global OOO00OO00OOOO000O #line:76
global O0O00OOO0OO000OOO #line:77
_OO0OOOO00000OOO00 ={CRITICAL :'CRITICAL',ERROR :'ERROR',WARNING :'WARNING',INFO :'INFO',DEBUG :'DEBUG',NOTSET :'NOTSET',}#line:87
_OO00OO0000OOOO0O0 ={'CRITICAL':CRITICAL ,'FATAL':FATAL ,'ERROR':ERROR ,'WARN':WARNING ,'WARNING':WARNING ,'INFO':INFO ,'DEBUG':DEBUG ,'NOTSET':NOTSET ,}#line:97
def getLevelName (OO0OO00000OO0O00O ):#line:99
    ""#line:116
    OO00O0OOO00O000O0 =_OO0OOOO00000OOO00 .get (OO0OO00000OO0O00O )#line:118
    if OO00O0OOO00O000O0 is not None :#line:119
        return OO00O0OOO00O000O0 #line:120
    OO00O0OOO00O000O0 =_OO00OO0000OOOO0O0 .get (OO0OO00000OO0O00O )#line:121
    if OO00O0OOO00O000O0 is not None :#line:122
        return OO00O0OOO00O000O0 #line:123
    return "Level %s"%OO0OO00000OO0O00O #line:124
def addLevelName (O0OO0OOOO000OO0O0 ,O00OOOOO0OO00OO0O ):#line:126
    ""#line:131
    _OO00OO000000OO0OO ()#line:132
    try :#line:133
        _OO0OOOO00000OOO00 [O0OO0OOOO000OO0O0 ]=O00OOOOO0OO00OO0O #line:134
        _OO00OO0000OOOO0O0 [O00OOOOO0OO00OO0O ]=O0OO0OOOO000OO0O0 #line:135
    finally :#line:136
        _OOO0OO0O0OO0OOO0O ()#line:137
if hasattr (sys ,'_getframe'):#line:139
    O0OO000OOOOO0OOO0 =lambda :sys ._getframe (3 )#line:140
else :#line:141
    def O0OO000OOOOO0OOO0 ():#line:142
        ""#line:143
        try :#line:144
            raise Exception #line:145
        except Exception :#line:146
            return sys .exc_info ()[2 ].tb_frame .f_back #line:147
_O00OOO00O0O00000O =os .path .normcase (addLevelName .__code__ .co_filename )#line:161
def _OOO0O00OOOO000OO0 (O0O00O0OOOOOO0000 ):#line:173
    if isinstance (O0O00O0OOOOOO0000 ,int ):#line:174
        O00000OO0OOOOO0OO =O0O00O0OOOOOO0000 #line:175
    elif str (O0O00O0OOOOOO0000 )==O0O00O0OOOOOO0000 :#line:176
        if O0O00O0OOOOOO0000 not in _OO00OO0000OOOO0O0 :#line:177
            raise ValueError ("Unknown level: %r"%O0O00O0OOOOOO0000 )#line:178
        O00000OO0OOOOO0OO =_OO00OO0000OOOO0O0 [O0O00O0OOOOOO0000 ]#line:179
    else :#line:180
        raise TypeError ("Level not an integer or a valid string: %r"%O0O00O0OOOOOO0000 )#line:181
    return O00000OO0OOOOO0OO #line:182
_O0OOO000OO0O00OO0 =threading .RLock ()#line:196
def _OO00OO000000OO0OO ():#line:198
    ""#line:203
    if _O0OOO000OO0O00OO0 :#line:204
        _O0OOO000OO0O00OO0 .acquire ()#line:205
def _OOO0OO0O0OO0OOO0O ():#line:207
    ""#line:210
    if _O0OOO000OO0O00OO0 :#line:211
        _O0OOO000OO0O00OO0 .release ()#line:212
if not hasattr (os ,'register_at_fork'):#line:217
    def _OOO0000O00OOOOO0O (OOOOO0000O0OO0OO0 ):#line:218
        pass #line:219
else :#line:220
    _O00000OO0OOO0O0O0 =weakref .WeakSet ()#line:226
    def _OOO0000O00OOOOO0O (O000O000000000000 ):#line:228
        _OO00OO000000OO0OO ()#line:229
        try :#line:230
            _O00000OO0OOO0O0O0 .add (O000O000000000000 )#line:231
        finally :#line:232
            _OOO0OO0O0OO0OOO0O ()#line:233
    def _OOOOO0O0O0OOOO00O ():#line:235
        for O000OOO0OO0O00OOO in _O00000OO0OOO0O0O0 :#line:237
            try :#line:238
                O000OOO0OO0O00OOO .createLock ()#line:239
            except Exception as O0O00O0OO00OO00OO :#line:240
                print ("Ignoring exception from logging atfork",instance ,"._reinit_lock() method:",O0O00O0OO00OO00OO ,file =sys .stderr )#line:243
        _OOO0OO0O0OO0OOO0O ()#line:244
    os .register_at_fork (before =_OO00OO000000OO0OO ,after_in_child =_OOOOO0O0O0OOOO00O ,after_in_parent =_OOO0OO0O0OO0OOO0O )#line:249
class LogRecord (object ):#line:256
    ""#line:267
    def __init__ (O00000000OO00O00O ,OOOO0O000OOOOO00O ,O00O0OOO0O0OOOOO0 ,O0O0OOO0OO0O000OO ,OO0OO0O0O0OO000OO ,O0OOO00O000O0OO0O ,O0O00000O000OO00O ,OOOO00O000O0OO00O ,func =None ,sinfo =None ,**OO0OOO000OO0O000O ):#line:269
        ""#line:272
        O0OOOO00000OO0O00 =time .time ()#line:273
        O00000000OO00O00O .name =OOOO0O000OOOOO00O #line:274
        O00000000OO00O00O .msg =O0OOO00O000O0OO0O #line:275
        if (O0O00000O000OO00O and len (O0O00000O000OO00O )==1 and isinstance (O0O00000O000OO00O [0 ],collections .abc .Mapping )and O0O00000O000OO00O [0 ]):#line:295
            O0O00000O000OO00O =O0O00000O000OO00O [0 ]#line:296
        O00000000OO00O00O .args =O0O00000O000OO00O #line:297
        O00000000OO00O00O .levelname =getLevelName (O00O0OOO0O0OOOOO0 )#line:298
        O00000000OO00O00O .levelno =O00O0OOO0O0OOOOO0 #line:299
        O00000000OO00O00O .pathname =O0O0OOO0OO0O000OO #line:300
        try :#line:301
            O00000000OO00O00O .filename =os .path .basename (O0O0OOO0OO0O000OO )#line:302
            O00000000OO00O00O .module =os .path .splitext (O00000000OO00O00O .filename )[0 ]#line:303
        except (TypeError ,ValueError ,AttributeError ):#line:304
            O00000000OO00O00O .filename =O0O0OOO0OO0O000OO #line:305
            O00000000OO00O00O .module ="Unknown module"#line:306
        O00000000OO00O00O .exc_info =OOOO00O000O0OO00O #line:307
        O00000000OO00O00O .exc_text =None #line:308
        O00000000OO00O00O .stack_info =sinfo #line:309
        O00000000OO00O00O .lineno =OO0OO0O0O0OO000OO #line:310
        O00000000OO00O00O .funcName =func #line:311
        O00000000OO00O00O .created =O0OOOO00000OO0O00 #line:312
        O00000000OO00O00O .msecs =(O0OOOO00000OO0O00 -int (O0OOOO00000OO0O00 ))*1000 #line:313
        O00000000OO00O00O .relativeCreated =(O00000000OO00O00O .created -_OOOO0000OO00000O0 )*1000 #line:314
        if OO0OOOO00OO0O0O0O :#line:315
            O00000000OO00O00O .thread =threading .get_ident ()#line:316
            O00000000OO00O00O .threadName =threading .current_thread ().name #line:317
        else :#line:318
            O00000000OO00O00O .thread =None #line:319
            O00000000OO00O00O .threadName =None #line:320
        if not O00OO00OOO0O0O000 :#line:321
            O00000000OO00O00O .processName =None #line:322
        else :#line:323
            O00000000OO00O00O .processName ='MainProcess'#line:324
            O0OOO00000000OO0O =sys .modules .get ('multiprocessing')#line:325
            if O0OOO00000000OO0O is not None :#line:326
                try :#line:331
                    O00000000OO00O00O .processName =O0OOO00000000OO0O .current_process ().name #line:332
                except Exception :#line:333
                    pass #line:334
        if O0O0OOOOO0OO00OOO and hasattr (os ,'getpid'):#line:335
            O00000000OO00O00O .process =os .getpid ()#line:336
        else :#line:337
            O00000000OO00O00O .process =None #line:338
    def __repr__ (O0OO0O0OO0O0OOO0O ):#line:340
        return '<LogRecord: %s, %s, %s, %s, "%s">'%(O0OO0O0OO0O0OOO0O .name ,O0OO0O0OO0O0OOO0O .levelno ,O0OO0O0OO0O0OOO0O .pathname ,O0OO0O0OO0O0OOO0O .lineno ,O0OO0O0OO0O0OOO0O .msg )#line:342
    def getMessage (O0000OOO0O00O0O0O ):#line:344
        ""#line:350
        O0O0OO0OOO0OOO0OO =str (O0000OOO0O00O0O0O .msg )#line:351
        if O0000OOO0O00O0O0O .args :#line:352
            O0O0OO0OOO0OOO0OO =O0O0OO0OOO0OOO0OO %O0000OOO0O00O0O0O .args #line:353
        return O0O0OO0OOO0OOO0OO #line:354
_OOO000OOOOOO00O0O =LogRecord #line:359
def setLogRecordFactory (OO0O0000OOOOO0OO0 ):#line:361
    ""#line:367
    global _OOO000OOOOOO00O0O #line:368
    _OOO000OOOOOO00O0O =OO0O0000OOOOO0OO0 #line:369
def getLogRecordFactory ():#line:371
    ""#line:374
    return _OOO000OOOOOO00O0O #line:376
def makeLogRecord (O00OO00OOO0O000O0 ):#line:378
    ""#line:384
    OO00OOO0OOOO00OO0 =_OOO000OOOOOO00O0O (None ,None ,"",0 ,"",(),None ,None )#line:385
    OO00OOO0OOOO00OO0 .__dict__ .update (O00OO00OOO0O000O0 )#line:386
    return OO00OOO0OOOO00OO0 #line:387
_O0O0OO00000OO000O =StrFormatter ()#line:393
del StrFormatter #line:394
class OOO0OOO0O0OOOOO0O (object ):#line:397
    default_format ='%(message)s'#line:399
    asctime_format ='%(asctime)s'#line:400
    asctime_search ='%(asctime)'#line:401
    validation_pattern =re .compile (r'%\(\w+\)[#0+ -]*(\*|\d+)?(\.(\*|\d+))?[diouxefgcrsa%]',re .I )#line:402
    def __init__ (OOOOOOO0O00O0OO0O ,O0O0OOOO0000O00O0 ):#line:404
        OOOOOOO0O00O0OO0O ._fmt =O0O0OOOO0000O00O0 or OOOOOOO0O00O0OO0O .default_format #line:405
    def usesTime (O0OO00OO00O000000 ):#line:407
        return O0OO00OO00O000000 ._fmt .find (O0OO00OO00O000000 .asctime_search )>=0 #line:408
    def validate (OOO0O0000OO0000O0 ):#line:410
        ""#line:411
        if not OOO0O0000OO0000O0 .validation_pattern .search (OOO0O0000OO0000O0 ._fmt ):#line:412
            raise ValueError ("Invalid format '%s' for '%s' style"%(OOO0O0000OO0000O0 ._fmt ,OOO0O0000OO0000O0 .default_format [0 ]))#line:413
    def _format (O0OO000O000O0O00O ,OOOOO0OO000O0O000 ):#line:415
        return O0OO000O000O0O00O ._fmt %OOOOO0OO000O0O000 .__dict__ #line:416
    def format (O00OO00O000000OO0 ,O000000O0OO0OOO00 ):#line:418
        try :#line:419
            return O00OO00O000000OO0 ._format (O000000O0OO0OOO00 )#line:420
        except KeyError as OO00O0O0O0O00O0O0 :#line:421
            raise ValueError ('Formatting field not found in record: %s'%OO00O0O0O0O00O0O0 )#line:422
class O0O0OO00OOO00OOO0 (OOO0OOO0O0OOOOO0O ):#line:425
    default_format ='{message}'#line:426
    asctime_format ='{asctime}'#line:427
    asctime_search ='{asctime'#line:428
    fmt_spec =re .compile (r'^(.?[<>=^])?[+ -]?#?0?(\d+|{\w+})?[,_]?(\.(\d+|{\w+}))?[bcdefgnosx%]?$',re .I )#line:430
    field_spec =re .compile (r'^(\d+|\w+)(\.\w+|\[[^]]+\])*$')#line:431
    def _format (O0000O0O0OO00OOO0 ,OO0OO000000OO000O ):#line:433
        return O0000O0O0OO00OOO0 ._fmt .format (**OO0OO000000OO000O .__dict__ )#line:434
    def validate (O0O0O00OO00OO0000 ):#line:436
        ""#line:437
        O0OO00O0OOO0000OO =set ()#line:438
        try :#line:439
            for _OOO00OO0OO00OO00O ,OOO0O0O000000O0OO ,OO0O0000OO0O0O0O0 ,O00OOOOOOOOOO0OO0 in _O0O0OO00000OO000O .parse (O0O0O00OO00OO0000 ._fmt ):#line:440
                if OOO0O0O000000O0OO :#line:441
                    if not O0O0O00OO00OO0000 .field_spec .match (OOO0O0O000000O0OO ):#line:442
                        raise ValueError ('invalid field name/expression: %r'%OOO0O0O000000O0OO )#line:443
                    O0OO00O0OOO0000OO .add (OOO0O0O000000O0OO )#line:444
                if O00OOOOOOOOOO0OO0 and O00OOOOOOOOOO0OO0 not in 'rsa':#line:445
                    raise ValueError ('invalid conversion: %r'%O00OOOOOOOOOO0OO0 )#line:446
                if OO0O0000OO0O0O0O0 and not O0O0O00OO00OO0000 .fmt_spec .match (OO0O0000OO0O0O0O0 ):#line:447
                    raise ValueError ('bad specifier: %r'%OO0O0000OO0O0O0O0 )#line:448
        except ValueError as O0O0O0O0O0O0O0O0O :#line:449
            raise ValueError ('invalid format: %s'%O0O0O0O0O0O0O0O0O )#line:450
        if not O0OO00O0OOO0000OO :#line:451
            raise ValueError ('invalid format: no fields')#line:452
class OO00O000OO00OO0OO (OOO0OOO0O0OOOOO0O ):#line:455
    default_format ='${message}'#line:456
    asctime_format ='${asctime}'#line:457
    asctime_search ='${asctime}'#line:458
    def __init__ (OOO00OOO00000OOOO ,OO0000OO0O00OO0O0 ):#line:460
        OOO00OOO00000OOOO ._fmt =OO0000OO0O00OO0O0 or OOO00OOO00000OOOO .default_format #line:461
        OOO00OOO00000OOOO ._tpl =Template (OOO00OOO00000OOOO ._fmt )#line:462
    def usesTime (O0OOO00OOO0O0O000 ):#line:464
        OO0O00OO00O0000O0 =O0OOO00OOO0O0O000 ._fmt #line:465
        return OO0O00OO00O0000O0 .find ('$asctime')>=0 or OO0O00OO00O0000O0 .find (O0OOO00OOO0O0O000 .asctime_format )>=0 #line:466
    def validate (OOO0O0OO00OOO00OO ):#line:468
        O0000O0000OO00000 =Template .pattern #line:469
        OO0OO00OOO0O0000O =set ()#line:470
        for OOO00OOO0O000O0OO in O0000O0000OO00000 .finditer (OOO0O0OO00OOO00OO ._fmt ):#line:471
            OO0OOO0O0OOO0OOOO =OOO00OOO0O000O0OO .groupdict ()#line:472
            if OO0OOO0O0OOO0OOOO ['named']:#line:473
                OO0OO00OOO0O0000O .add (OO0OOO0O0OOO0OOOO ['named'])#line:474
            elif OO0OOO0O0OOO0OOOO ['braced']:#line:475
                OO0OO00OOO0O0000O .add (OO0OOO0O0OOO0OOOO ['braced'])#line:476
            elif OOO00OOO0O000O0OO .group (0 )=='$':#line:477
                raise ValueError ('invalid format: bare \'$\' not allowed')#line:478
        if not OO0OO00OOO0O0000O :#line:479
            raise ValueError ('invalid format: no fields')#line:480
    def _format (OO00O0O0OOO0O000O ,OO00O00OOO00O00OO ):#line:482
        return OO00O0O0OOO0O000O ._tpl .substitute (**OO00O00OOO00O00OO .__dict__ )#line:483
BASIC_FORMAT ="%(levelname)s:%(name)s:%(message)s"#line:486
_OOO0O0000O0000O00 ={'%':(OOO0OOO0O0OOOOO0O ,BASIC_FORMAT ),'{':(O0O0OO00OOO00OOO0 ,'{levelname}:{name}:{message}'),'$':(OO00O000OO00OO0OO ,'${levelname}:${name}:${message}'),}#line:492
class Formatter (object ):#line:494
    ""#line:535
    converter =time .localtime #line:537
    def __init__ (O0OO0O0OO0O0000O0 ,fmt =None ,datefmt =None ,style ='%',validate =True ):#line:539
        ""#line:554
        if style not in _OOO0O0000O0000O00 :#line:555
            raise ValueError ('Style must be one of: %s'%','.join (_OOO0O0000O0000O00 .keys ()))#line:557
        O0OO0O0OO0O0000O0 ._style =_OOO0O0000O0000O00 [style ][0 ](fmt )#line:558
        if validate :#line:559
            O0OO0O0OO0O0000O0 ._style .validate ()#line:560
        O0OO0O0OO0O0000O0 ._fmt =O0OO0O0OO0O0000O0 ._style ._fmt #line:562
        O0OO0O0OO0O0000O0 .datefmt =datefmt #line:563
    default_time_format ='%Y-%m-%d %H:%M:%S'#line:565
    default_msec_format ='%s,%03d'#line:566
    def formatTime (O0OO000000O0O00O0 ,OOO0OOO0O0000O00O ,datefmt =None ):#line:568
        ""#line:585
        O0OO00O0O00O0O00O =O0OO000000O0O00O0 .converter (OOO0OOO0O0000O00O .created )#line:586
        if datefmt :#line:587
            O0000OO0O00O0OOO0 =time .strftime (datefmt ,O0OO00O0O00O0O00O )#line:588
        else :#line:589
            O000OO00000O0O00O =time .strftime (O0OO000000O0O00O0 .default_time_format ,O0OO00O0O00O0O00O )#line:590
            O0000OO0O00O0OOO0 =O0OO000000O0O00O0 .default_msec_format %(O000OO00000O0O00O ,OOO0OOO0O0000O00O .msecs )#line:591
        return O0000OO0O00O0OOO0 #line:592
    def formatException (O00OO000OO00OO0OO ,O000OO0O0000O0O0O ):#line:594
        ""#line:600
        O0O0O000OOOOO0O00 =io .StringIO ()#line:601
        OO0OOO0OO00OO0OOO =O000OO0O0000O0O0O [2 ]#line:602
        traceback .print_exception (O000OO0O0000O0O0O [0 ],O000OO0O0000O0O0O [1 ],OO0OOO0OO00OO0OOO ,None ,O0O0O000OOOOO0O00 )#line:606
        OO0O0OO0000O0O0O0 =O0O0O000OOOOO0O00 .getvalue ()#line:607
        O0O0O000OOOOO0O00 .close ()#line:608
        if OO0O0OO0000O0O0O0 [-1 :]=="\n":#line:609
            OO0O0OO0000O0O0O0 =OO0O0OO0000O0O0O0 [:-1 ]#line:610
        return OO0O0OO0000O0O0O0 #line:611
    def usesTime (O0000OO0O0O00OO0O ):#line:613
        ""#line:616
        return O0000OO0O0O00OO0O ._style .usesTime ()#line:617
    def formatMessage (OOO00OOO0O00OOO0O ,OO0O0O0OOOO0OOO0O ):#line:619
        return OOO00OOO0O00OOO0O ._style .format (OO0O0O0OOOO0OOO0O )#line:620
    def formatStack (O0O0OO0OO000OOO00 ,O0O0O00O0OO00000O ):#line:622
        ""#line:632
        return O0O0O00O0OO00000O #line:633
    def format (O0O0O0000OOOOOO0O ,OOO000O0O0O00O0O0 ):#line:635
        ""#line:647
        OOO000O0O0O00O0O0 .message =OOO000O0O0O00O0O0 .getMessage ()#line:648
        if O0O0O0000OOOOOO0O .usesTime ():#line:649
            OOO000O0O0O00O0O0 .asctime =O0O0O0000OOOOOO0O .formatTime (OOO000O0O0O00O0O0 ,O0O0O0000OOOOOO0O .datefmt )#line:650
        OOOO00OOO00OO0000 =O0O0O0000OOOOOO0O .formatMessage (OOO000O0O0O00O0O0 )#line:651
        print (OOOO00OOO00OO0000 )#line:652
        if OOO000O0O0O00O0O0 .exc_info :#line:653
            if not OOO000O0O0O00O0O0 .exc_text :#line:656
                OOO000O0O0O00O0O0 .exc_text =O0O0O0000OOOOOO0O .formatException (OOO000O0O0O00O0O0 .exc_info )#line:657
        if OOO000O0O0O00O0O0 .exc_text :#line:658
            if OOOO00OOO00OO0000 [-1 :]!="\n":#line:659
                OOOO00OOO00OO0000 =OOOO00OOO00OO0000 +"\n"#line:660
            OOOO00OOO00OO0000 =OOOO00OOO00OO0000 +OOO000O0O0O00O0O0 .exc_text #line:661
        if OOO000O0O0O00O0O0 .stack_info :#line:662
            if OOOO00OOO00OO0000 [-1 :]!="\n":#line:663
                OOOO00OOO00OO0000 =OOOO00OOO00OO0000 +"\n"#line:664
            OOOO00OOO00OO0000 =OOOO00OOO00OO0000 +O0O0O0000OOOOOO0O .formatStack (OOO000O0O0O00O0O0 .stack_info )#line:665
        return OOOO00OOO00OO0000 #line:666
_O0O00000000OOO000 =Formatter ()#line:671
class BufferingFormatter (object ):#line:673
    ""#line:676
    def __init__ (OO00OO00OOO0O0OOO ,linefmt =None ):#line:677
        ""#line:681
        if linefmt :#line:682
            OO00OO00OOO0O0OOO .linefmt =linefmt #line:683
        else :#line:684
            OO00OO00OOO0O0OOO .linefmt =_O0O00000000OOO000 #line:685
    def formatHeader (O00OO00OOOOO0O000 ,O0000O0O0O00OOOO0 ):#line:687
        ""#line:690
        return ""#line:691
    def formatFooter (OOOO0O000O000OO0O ,OOO00OOO00O0OOO0O ):#line:693
        ""#line:696
        return ""#line:697
    def format (OO000OO000O0OOO0O ,O000O0OO0O0000OO0 ):#line:699
        ""#line:702
        OOO0O0O000O0O000O =""#line:703
        if len (O000O0OO0O0000OO0 )>0 :#line:704
            OOO0O0O000O0O000O =OOO0O0O000O0O000O +OO000OO000O0OOO0O .formatHeader (O000O0OO0O0000OO0 )#line:705
            for O000O000OOO0O0000 in O000O0OO0O0000OO0 :#line:706
                OOO0O0O000O0O000O =OOO0O0O000O0O000O +OO000OO000O0OOO0O .linefmt .format (O000O000OOO0O0000 )#line:707
            OOO0O0O000O0O000O =OOO0O0O000O0O000O +OO000OO000O0OOO0O .formatFooter (O000O0OO0O0000OO0 )#line:708
        return OOO0O0O000O0O000O #line:709
class Filter (object ):#line:715
    ""#line:725
    def __init__ (O0000OOO000O000O0 ,name =''):#line:726
        ""#line:733
        O0000OOO000O000O0 .name =name #line:734
        O0000OOO000O000O0 .nlen =len (name )#line:735
    def filter (OOO000OOOOO000000 ,OOO0O00OOO000O0OO ):#line:737
        ""#line:743
        if OOO000OOOOO000000 .nlen ==0 :#line:744
            return True #line:745
        elif OOO000OOOOO000000 .name ==OOO0O00OOO000O0OO .name :#line:746
            return True #line:747
        elif OOO0O00OOO000O0OO .name .find (OOO000OOOOO000000 .name ,0 ,OOO000OOOOO000000 .nlen )!=0 :#line:748
            return False #line:749
        return (OOO0O00OOO000O0OO .name [OOO000OOOOO000000 .nlen ]==".")#line:750
class O000000O00OOO000O (object ):#line:752
    ""#line:756
    def __init__ (O0000O0O0O0OO000O ):#line:757
        ""#line:760
        O0000O0O0O0OO000O .filters =[]#line:761
    def addFilter (OO0000O000000O00O ,OO0O00O0O0OO00OOO ):#line:763
        ""#line:766
        if not (OO0O00O0O0OO00OOO in OO0000O000000O00O .filters ):#line:767
            OO0000O000000O00O .filters .append (OO0O00O0O0OO00OOO )#line:768
    def removeFilter (O0OOO0OO0O0O0000O ,O0OO00O00O0O0O000 ):#line:770
        ""#line:773
        if O0OO00O00O0O0O000 in O0OOO0OO0O0O0000O .filters :#line:774
            O0OOO0OO0O0O0000O .filters .remove (O0OO00O00O0O0O000 )#line:775
    def filter (OO00O00OOO0OOO0OO ,OOOOOO000O00O00OO ):#line:777
        ""#line:788
        OO0O0OO0OOOO00000 =True #line:789
        for O00OO000OO00000OO in OO00O00OOO0OOO0OO .filters :#line:790
            if hasattr (O00OO000OO00000OO ,'filter'):#line:791
                OOO00000OOOOO0O00 =O00OO000OO00000OO .filter (OOOOOO000O00O00OO )#line:792
            else :#line:793
                OOO00000OOOOO0O00 =O00OO000OO00000OO (OOOOOO000O00O00OO )#line:794
            if not OOO00000OOOOO0O00 :#line:795
                OO0O0OO0OOOO00000 =False #line:796
                break #line:797
        return OO0O0OO0OOOO00000 #line:798
_O0O00O00O0O0O0O0O =weakref .WeakValueDictionary ()#line:804
_OOO000000O0OO0000 =[]#line:805
def _OOOO0000O0OOOOO0O (OOO0O00OO0O0O0O0O ):#line:807
    ""#line:810
    O0OOO0OOOOOO0OOOO ,OOOO0OOO0OO00OO0O ,OOOO0O0O0O0O000O0 =_OO00OO000000OO0OO ,_OOO0OO0O0OO0OOO0O ,_OOO000000O0OO0000 #line:815
    if O0OOO0OOOOOO0OOOO and OOOO0OOO0OO00OO0O and OOOO0O0O0O0O000O0 :#line:816
        O0OOO0OOOOOO0OOOO ()#line:817
        try :#line:818
            if OOO0O00OO0O0O0O0O in OOOO0O0O0O0O000O0 :#line:819
                OOOO0O0O0O0O000O0 .remove (OOO0O00OO0O0O0O0O )#line:820
        finally :#line:821
            OOOO0OOO0OO00OO0O ()#line:822
def _OO00OO00000000O0O (OO0O0O0OOOO000O00 ):#line:824
    ""#line:827
    _OO00OO000000OO0OO ()#line:828
    try :#line:829
        _OOO000000O0OO0000 .append (weakref .ref (OO0O0O0OOOO000O00 ,_OOOO0000O0OOOOO0O ))#line:830
    finally :#line:831
        _OOO0OO0O0OO0OOO0O ()#line:832
class Handler (O000000O00OOO000O ):#line:834
    ""#line:842
    def __init__ (O0O000OO0OOO00OO0 ,level =NOTSET ):#line:843
        ""#line:847
        O000000O00OOO000O .__init__ (O0O000OO0OOO00OO0 )#line:848
        O0O000OO0OOO00OO0 ._name =None #line:849
        O0O000OO0OOO00OO0 .level =_OOO0O00OOOO000OO0 (level )#line:850
        O0O000OO0OOO00OO0 .formatter =None #line:851
        _OO00OO00000000O0O (O0O000OO0OOO00OO0 )#line:853
        O0O000OO0OOO00OO0 .createLock ()#line:854
    def get_name (O0O00OOOO0O00OOO0 ):#line:856
        return O0O00OOOO0O00OOO0 ._name #line:857
    def set_name (O000OOOO0OOO0OOO0 ,O000OOO0000OO0000 ):#line:859
        _OO00OO000000OO0OO ()#line:860
        try :#line:861
            if O000OOOO0OOO0OOO0 ._name in _O0O00O00O0O0O0O0O :#line:862
                del _O0O00O00O0O0O0O0O [O000OOOO0OOO0OOO0 ._name ]#line:863
            O000OOOO0OOO0OOO0 ._name =O000OOO0000OO0000 #line:864
            if O000OOO0000OO0000 :#line:865
                _O0O00O00O0O0O0O0O [O000OOO0000OO0000 ]=O000OOOO0OOO0OOO0 #line:866
        finally :#line:867
            _OOO0OO0O0OO0OOO0O ()#line:868
    name =property (get_name ,set_name )#line:870
    def createLock (O0O00OO0OO00O000O ):#line:872
        ""#line:875
        O0O00OO0OO00O000O .lock =threading .RLock ()#line:876
        _OOO0000O00OOOOO0O (O0O00OO0OO00O000O )#line:877
    def acquire (OO00000O000O00OO0 ):#line:879
        ""#line:882
        if OO00000O000O00OO0 .lock :#line:883
            OO00000O000O00OO0 .lock .acquire ()#line:884
    def release (OO0O00OO00OOOOOOO ):#line:886
        ""#line:889
        if OO0O00OO00OOOOOOO .lock :#line:890
            OO0O00OO00OOOOOOO .lock .release ()#line:891
    def setLevel (OOO0O00OO0O0000OO ,OOOO00OOO00O0OO00 ):#line:893
        ""#line:896
        OOO0O00OO0O0000OO .level =_OOO0O00OOOO000OO0 (OOOO00OOO00O0OO00 )#line:897
    def format (O0000O0OOOO0O0OOO ,O00OOO0000OOO0OOO ):#line:899
        ""#line:905
        if O0000O0OOOO0O0OOO .formatter :#line:906
            OOO00O0OOOOOOO00O =O0000O0OOOO0O0OOO .formatter #line:907
        else :#line:908
            OOO00O0OOOOOOO00O =_O0O00000000OOO000 #line:909
        return OOO00O0OOOOOOO00O .format (O00OOO0000OOO0OOO )#line:910
    def emit (OO0OO0000O0000OOO ,O0O0000OO00O00O0O ):#line:912
        ""#line:918
        raise NotImplementedError ('emit must be implemented ' 'by Handler subclasses')#line:920
    def handle (OO0000O0OO000O00O ,O0OOO00OOOOO0O000 ):#line:922
        ""#line:930
        O0OO0000O0OO0OOO0 =OO0000O0OO000O00O .filter (O0OOO00OOOOO0O000 )#line:931
        if O0OO0000O0OO0OOO0 :#line:932
            OO0000O0OO000O00O .acquire ()#line:933
            try :#line:934
                OO0000O0OO000O00O .emit (O0OOO00OOOOO0O000 )#line:935
            finally :#line:936
                OO0000O0OO000O00O .release ()#line:937
        return O0OO0000O0OO0OOO0 #line:938
    def setFormatter (OO000OO000O0OOOO0 ,O0000O00OO0O000OO ):#line:940
        ""#line:943
        OO000OO000O0OOOO0 .formatter =O0000O00OO0O000OO #line:944
    def flush (OOOOO00OO0O00O0OO ):#line:946
        ""#line:952
        pass #line:953
    def close (OO0000OO00O0OO0OO ):#line:955
        ""#line:963
        _OO00OO000000OO0OO ()#line:965
        try :#line:966
            if OO0000OO00O0OO0OO ._name and OO0000OO00O0OO0OO ._name in _O0O00O00O0O0O0O0O :#line:967
                del _O0O00O00O0O0O0O0O [OO0000OO00O0OO0OO ._name ]#line:968
        finally :#line:969
            _OOO0OO0O0OO0OOO0O ()#line:970
    def handleError (OOOO00O00O000OOO0 ,OOO0O0OOO0O0OO0OO ):#line:972
        ""#line:983
        if raiseExceptions and sys .stderr :#line:984
            O0O0OOOOO0O000OOO ,O00OO00000O0OO000 ,OO0000000O0O0O00O =sys .exc_info ()#line:985
            try :#line:986
                sys .stderr .write ('--- Logging error ---\n')#line:987
                traceback .print_exception (O0O0OOOOO0O000OOO ,O00OO00000O0OO000 ,OO0000000O0O0O00O ,None ,sys .stderr )#line:988
                sys .stderr .write ('Call stack:\n')#line:989
                OOOOOOO00OO0O0OO0 =OO0000000O0O0O00O .tb_frame #line:992
                while (OOOOOOO00OO0O0OO0 and os .path .dirname (OOOOOOO00OO0O0OO0 .f_code .co_filename )==__path__ [0 ]):#line:994
                    OOOOOOO00OO0O0OO0 =OOOOOOO00OO0O0OO0 .f_back #line:995
                if OOOOOOO00OO0O0OO0 :#line:996
                    traceback .print_stack (OOOOOOO00OO0O0OO0 ,file =sys .stderr )#line:997
                else :#line:998
                    sys .stderr .write ('Logged from file %s, line %s\n'%(OOO0O0OOO0O0OO0OO .filename ,OOO0O0OOO0O0OO0OO .lineno ))#line:1001
                try :#line:1003
                    sys .stderr .write ('Message: %r\n' 'Arguments: %s\n'%(OOO0O0OOO0O0OO0OO .msg ,OOO0O0OOO0O0OO0OO .args ))#line:1006
                except RecursionError :#line:1007
                    raise #line:1008
                except Exception :#line:1009
                    sys .stderr .write ('Unable to print the message and arguments' ' - possible formatting error.\nUse the' ' traceback above to help find the error.\n')#line:1013
            except OSError :#line:1014
                pass #line:1015
            finally :#line:1016
                del O0O0OOOOO0O000OOO ,O00OO00000O0OO000 ,OO0000000O0O0O00O #line:1017
    def __repr__ (O0O000O00O0O00000 ):#line:1019
        OO0000O00O00O0O0O =getLevelName (O0O000O00O0O00000 .level )#line:1020
        return '<%s (%s)>'%(O0O000O00O0O00000 .__class__ .__name__ ,OO0000O00O00O0O0O )#line:1021
class StreamHandler (Handler ):#line:1023
    ""#line:1028
    terminator ='\n'#line:1030
    def __init__ (O0O0OO00O0000OO00 ,stream =None ):#line:1032
        ""#line:1037
        Handler .__init__ (O0O0OO00O0000OO00 )#line:1038
        if stream is None :#line:1039
            stream =sys .stderr #line:1040
        O0O0OO00O0000OO00 .stream =stream #line:1041
    def flush (OOOO000OOOOOOO000 ):#line:1043
        ""#line:1046
        OOOO000OOOOOOO000 .acquire ()#line:1047
        try :#line:1048
            if OOOO000OOOOOOO000 .stream and hasattr (OOOO000OOOOOOO000 .stream ,"flush"):#line:1049
                OOOO000OOOOOOO000 .stream .flush ()#line:1050
        finally :#line:1051
            OOOO000OOOOOOO000 .release ()#line:1052
    def emit (O0OOOOO0OO0OOO00O ,O00O0O0OO00O00O0O ):#line:1054
        ""#line:1064
        try :#line:1065
            O00O0000OO00OOO00 =O0OOOOO0OO0OOO00O .format (O00O0O0OO00O00O0O )#line:1066
            OO00O00OO00000000 =O0OOOOO0OO0OOO00O .stream #line:1067
            OO00O00OO00000000 .write (O00O0000OO00OOO00 +O0OOOOO0OO0OOO00O .terminator )#line:1069
            O0OOOOO0OO0OOO00O .flush ()#line:1070
        except RecursionError :#line:1071
            raise #line:1072
        except Exception :#line:1073
            O0OOOOO0OO0OOO00O .handleError (O00O0O0OO00O00O0O )#line:1074
    def setStream (OOO000OOOO0OOOO0O ,O00OO00OO0OOOO0O0 ):#line:1076
        ""#line:1083
        if O00OO00OO0OOOO0O0 is OOO000OOOO0OOOO0O .stream :#line:1084
            OO0000OOO0O00OOO0 =None #line:1085
        else :#line:1086
            OO0000OOO0O00OOO0 =OOO000OOOO0OOOO0O .stream #line:1087
            OOO000OOOO0OOOO0O .acquire ()#line:1088
            try :#line:1089
                OOO000OOOO0OOOO0O .flush ()#line:1090
                OOO000OOOO0OOOO0O .stream =O00OO00OO0OOOO0O0 #line:1091
            finally :#line:1092
                OOO000OOOO0OOOO0O .release ()#line:1093
        return OO0000OOO0O00OOO0 #line:1094
    def __repr__ (OO0OOOO0O00OO00O0 ):#line:1096
        O0000OO0O000OO000 =getLevelName (OO0OOOO0O00OO00O0 .level )#line:1097
        OO0000OOOO0O0OO0O =getattr (OO0OOOO0O00OO00O0 .stream ,'name','')#line:1098
        OO0000OOOO0O0OO0O =str (OO0000OOOO0O0OO0O )#line:1100
        if OO0000OOOO0O0OO0O :#line:1101
            OO0000OOOO0O0OO0O +=' '#line:1102
        return '<%s %s(%s)>'%(OO0OOOO0O00OO00O0 .__class__ .__name__ ,OO0000OOOO0O0OO0O ,O0000OO0O000OO000 )#line:1103
class FileHandler (StreamHandler ):#line:1106
    ""#line:1109
    def __init__ (OOO0O0OOOOOO0O00O ,O0000O0O0OO00000O ,mode ='a',encoding =None ,delay =False ):#line:1110
        ""#line:1113
        O0000O0O0OO00000O =os .fspath (O0000O0O0OO00000O )#line:1115
        OOO0O0OOOOOO0O00O .baseFilename =os .path .abspath (O0000O0O0OO00000O )#line:1118
        OOO0O0OOOOOO0O00O .mode =mode #line:1119
        OOO0O0OOOOOO0O00O .encoding =encoding #line:1120
        OOO0O0OOOOOO0O00O .delay =delay #line:1121
        if delay :#line:1122
            Handler .__init__ (OOO0O0OOOOOO0O00O )#line:1125
            OOO0O0OOOOOO0O00O .stream =None #line:1126
        else :#line:1127
            StreamHandler .__init__ (OOO0O0OOOOOO0O00O ,OOO0O0OOOOOO0O00O ._open ())#line:1128
    def close (O00O0O0OO0O0000OO ):#line:1130
        ""#line:1133
        O00O0O0OO0O0000OO .acquire ()#line:1134
        try :#line:1135
            try :#line:1136
                if O00O0O0OO0O0000OO .stream :#line:1137
                    try :#line:1138
                        O00O0O0OO0O0000OO .flush ()#line:1139
                    finally :#line:1140
                        OOO000O0000OOOOOO =O00O0O0OO0O0000OO .stream #line:1141
                        O00O0O0OO0O0000OO .stream =None #line:1142
                        if hasattr (OOO000O0000OOOOOO ,"close"):#line:1143
                            OOO000O0000OOOOOO .close ()#line:1144
            finally :#line:1145
                StreamHandler .close (O00O0O0OO0O0000OO )#line:1148
        finally :#line:1149
            O00O0O0OO0O0000OO .release ()#line:1150
    def _open (OO0O0O00O0OOO000O ):#line:1152
        ""#line:1156
        return open (OO0O0O00O0OOO000O .baseFilename ,OO0O0O00O0OOO000O .mode ,encoding =OO0O0O00O0OOO000O .encoding )#line:1157
    def emit (OO00OOOO000OO0O00 ,O000OOOO0OO00OO00 ):#line:1159
        ""#line:1165
        if OO00OOOO000OO0O00 .stream is None :#line:1166
            OO00OOOO000OO0O00 .stream =OO00OOOO000OO0O00 ._open ()#line:1167
        StreamHandler .emit (OO00OOOO000OO0O00 ,O000OOOO0OO00OO00 )#line:1168
    def __repr__ (O000O00OOO000O0O0 ):#line:1170
        O0O000OO00O0OO00O =getLevelName (O000O00OOO000O0O0 .level )#line:1171
        return '<%s %s (%s)>'%(O000O00OOO000O0O0 .__class__ .__name__ ,O000O00OOO000O0O0 .baseFilename ,O0O000OO00O0OO00O )#line:1172
class _OO00OO00O00O0O0OO (StreamHandler ):#line:1175
    ""#line:1180
    def __init__ (OOO0OO00OOOOO00O0 ,level =NOTSET ):#line:1181
        ""#line:1184
        Handler .__init__ (OOO0OO00OOOOO00O0 ,level )#line:1185
    @property #line:1187
    def stream (O0000OOO00O000O0O ):#line:1188
        return sys .stderr #line:1189
_OO0O00O0OO000000O =_OO00OO00O00O0O0OO (WARNING )#line:1192
lastResort =_OO0O00O0OO000000O #line:1193
class O000OOOOOOOO0O00O (object ):#line:1199
    ""#line:1204
    def __init__ (O0OOOOO0O0O0OOO00 ,O0O00O0OOOO00O00O ):#line:1205
        ""#line:1208
        O0OOOOO0O0O0OOO00 .loggerMap ={O0O00O0OOOO00O00O :None }#line:1209
    def append (O0O000O0OOO00000O ,O000OO00OO0000OO0 ):#line:1211
        ""#line:1214
        if O000OO00OO0000OO0 not in O0O000O0OOO00000O .loggerMap :#line:1215
            O0O000O0OOO00000O .loggerMap [O000OO00OO0000OO0 ]=None #line:1216
def setLoggerClass (O000OO0O000OOOOOO ):#line:1222
    ""#line:1227
    if O000OO0O000OOOOOO !=Logger :#line:1228
        if not issubclass (O000OO0O000OOOOOO ,Logger ):#line:1229
            raise TypeError ("logger not derived from logging.Logger: "+O000OO0O000OOOOOO .__name__ )#line:1231
    global _OO00OOOO00OO000OO #line:1232
    _OO00OOOO00OO000OO =O000OO0O000OOOOOO #line:1233
def getLoggerClass ():#line:1235
    ""#line:1238
    return _OO00OOOO00OO000OO #line:1239
class O0OO00O00O00O0OOO (object ):#line:1241
    ""#line:1245
    def __init__ (OOO000O00000O0O0O ,OO00OOOOOO0OOO000 ):#line:1246
        ""#line:1249
        OOO000O00000O0O0O .root =OO00OOOOOO0OOO000 #line:1250
        OOO000O00000O0O0O .disable =0 #line:1251
        OOO000O00000O0O0O .emittedNoHandlerWarning =False #line:1252
        OOO000O00000O0O0O .loggerDict ={}#line:1253
        OOO000O00000O0O0O .loggerClass =None #line:1254
        OOO000O00000O0O0O .logRecordFactory =None #line:1255
    @property #line:1257
    def disable (OOOOOO00O0O0O000O ):#line:1258
        return OOOOOO00O0O0O000O ._disable #line:1259
    @disable .setter #line:1261
    def disable (OOOO000O00O0O0O00 ,OOO0OO000OO0O0000 ):#line:1262
        OOOO000O00O0O0O00 ._disable =_OOO0O00OOOO000OO0 (OOO0OO000OO0O0000 )#line:1263
    def getLogger (O0O000OO00O0O0OO0 ,O0OOO00O000O0000O ):#line:1265
        ""#line:1275
        O00OO0O00OO00OOOO =None #line:1276
        if not isinstance (O0OOO00O000O0000O ,str ):#line:1277
            raise TypeError ('A logger name must be a string')#line:1278
        _OO00OO000000OO0OO ()#line:1279
        try :#line:1280
            if O0OOO00O000O0000O in O0O000OO00O0O0OO0 .loggerDict :#line:1281
                O00OO0O00OO00OOOO =O0O000OO00O0O0OO0 .loggerDict [O0OOO00O000O0000O ]#line:1282
                if isinstance (O00OO0O00OO00OOOO ,O000OOOOOOOO0O00O ):#line:1283
                    O00OOOO00OO00000O =O00OO0O00OO00OOOO #line:1284
                    O00OO0O00OO00OOOO =(O0O000OO00O0O0OO0 .loggerClass or _OO00OOOO00OO000OO )(O0OOO00O000O0000O )#line:1285
                    O00OO0O00OO00OOOO .manager =O0O000OO00O0O0OO0 #line:1286
                    O0O000OO00O0O0OO0 .loggerDict [O0OOO00O000O0000O ]=O00OO0O00OO00OOOO #line:1287
                    O0O000OO00O0O0OO0 ._fixupChildren (O00OOOO00OO00000O ,O00OO0O00OO00OOOO )#line:1288
                    O0O000OO00O0O0OO0 ._fixupParents (O00OO0O00OO00OOOO )#line:1289
            else :#line:1290
                O00OO0O00OO00OOOO =(O0O000OO00O0O0OO0 .loggerClass or _OO00OOOO00OO000OO )(O0OOO00O000O0000O )#line:1291
                O00OO0O00OO00OOOO .manager =O0O000OO00O0O0OO0 #line:1292
                O0O000OO00O0O0OO0 .loggerDict [O0OOO00O000O0000O ]=O00OO0O00OO00OOOO #line:1293
                O0O000OO00O0O0OO0 ._fixupParents (O00OO0O00OO00OOOO )#line:1294
        finally :#line:1295
            _OOO0OO0O0OO0OOO0O ()#line:1296
        return O00OO0O00OO00OOOO #line:1297
    def setLoggerClass (O0OOOO000OO00O000 ,OO000OOO000OOO0OO ):#line:1299
        ""#line:1302
        if OO000OOO000OOO0OO !=Logger :#line:1303
            if not issubclass (OO000OOO000OOO0OO ,Logger ):#line:1304
                raise TypeError ("logger not derived from logging.Logger: "+OO000OOO000OOO0OO .__name__ )#line:1306
        O0OOOO000OO00O000 .loggerClass =OO000OOO000OOO0OO #line:1307
    def setLogRecordFactory (O0O0O0OO000O0O0O0 ,O0OO00OOO00000O0O ):#line:1309
        ""#line:1313
        O0O0O0OO000O0O0O0 .logRecordFactory =O0OO00OOO00000O0O #line:1314
    def _fixupParents (OOO00OOOOO0O0O0O0 ,OOO0O0OOO0OOO00O0 ):#line:1316
        ""#line:1320
        O0O000OO0OOOOO000 =OOO0O0OOO0OOO00O0 .name #line:1321
        O0O0OOO000OO00OOO =O0O000OO0OOOOO000 .rfind (".")#line:1322
        O0O00O00OO000OO0O =None #line:1323
        while (O0O0OOO000OO00OOO >0 )and not O0O00O00OO000OO0O :#line:1324
            O0OO0000O0O0000O0 =O0O000OO0OOOOO000 [:O0O0OOO000OO00OOO ]#line:1325
            if O0OO0000O0O0000O0 not in OOO00OOOOO0O0O0O0 .loggerDict :#line:1326
                OOO00OOOOO0O0O0O0 .loggerDict [O0OO0000O0O0000O0 ]=O000OOOOOOOO0O00O (OOO0O0OOO0OOO00O0 )#line:1327
            else :#line:1328
                O00000OOOOOOO0OO0 =OOO00OOOOO0O0O0O0 .loggerDict [O0OO0000O0O0000O0 ]#line:1329
                if isinstance (O00000OOOOOOO0OO0 ,Logger ):#line:1330
                    O0O00O00OO000OO0O =O00000OOOOOOO0OO0 #line:1331
                else :#line:1332
                    assert isinstance (O00000OOOOOOO0OO0 ,O000OOOOOOOO0O00O )#line:1333
                    O00000OOOOOOO0OO0 .append (OOO0O0OOO0OOO00O0 )#line:1334
            O0O0OOO000OO00OOO =O0O000OO0OOOOO000 .rfind (".",0 ,O0O0OOO000OO00OOO -1 )#line:1335
        if not O0O00O00OO000OO0O :#line:1336
            O0O00O00OO000OO0O =OOO00OOOOO0O0O0O0 .root #line:1337
        OOO0O0OOO0OOO00O0 .parent =O0O00O00OO000OO0O #line:1338
    def _fixupChildren (O00O00OO00OO0O0OO ,O000OOOOOOO0O0000 ,OO000O0OOOOO0OOOO ):#line:1340
        ""#line:1344
        O00O0OO0O0OO00O00 =OO000O0OOOOO0OOOO .name #line:1345
        O0000OO0O0OO0O0OO =len (O00O0OO0O0OO00O00 )#line:1346
        for O0O000000OOO000OO in O000OOOOOOO0O0000 .loggerMap .keys ():#line:1347
            if O0O000000OOO000OO .parent .name [:O0000OO0O0OO0O0OO ]!=O00O0OO0O0OO00O00 :#line:1349
                OO000O0OOOOO0OOOO .parent =O0O000000OOO000OO .parent #line:1350
                O0O000000OOO000OO .parent =OO000O0OOOOO0OOOO #line:1351
    def _clear_cache (O0OO0OOOO0OOOO0OO ):#line:1353
        ""#line:1357
        _OO00OO000000OO0OO ()#line:1359
        for OO00O0O00O0OOOO00 in O0OO0OOOO0OOOO0OO .loggerDict .values ():#line:1360
            if isinstance (OO00O0O00O0OOOO00 ,Logger ):#line:1361
                OO00O0O00O0OOOO00 ._cache .clear ()#line:1362
        O0OO0OOOO0OOOO0OO .root ._cache .clear ()#line:1363
        _OOO0OO0O0OO0OOO0O ()#line:1364
class Logger (O000000O00OOO000O ):#line:1370
    ""#line:1384
    def __init__ (OOOO0O00OO000000O ,O000O00O0O0O0OOO0 ,level =NOTSET ):#line:1385
        ""#line:1388
        O000000O00OOO000O .__init__ (OOOO0O00OO000000O )#line:1389
        OOOO0O00OO000000O .name =O000O00O0O0O0OOO0 #line:1390
        OOOO0O00OO000000O .level =_OOO0O00OOOO000OO0 (level )#line:1391
        OOOO0O00OO000000O .parent =None #line:1392
        OOOO0O00OO000000O .propagate =True #line:1393
        OOOO0O00OO000000O .handlers =[]#line:1394
        OOOO0O00OO000000O .disabled =False #line:1395
        OOOO0O00OO000000O ._cache ={}#line:1396
    def setLevel (O0OOOO0O0O0OO0OO0 ,OOO00OO0OO000OOOO ):#line:1398
        ""#line:1401
        O0OOOO0O0O0OO0OO0 .level =_OOO0O00OOOO000OO0 (OOO00OO0OO000OOOO )#line:1402
        O0OOOO0O0O0OO0OO0 .manager ._clear_cache ()#line:1403
    def debug (O0OO00OO00OO0OO00 ,OO00O0O0O0OO0O000 ,*O00O0OOOO0O00000O ,**O0O0OOO0O000O0OO0 ):#line:1405
        ""#line:1413
        global OO000O0OOOO00O0OO #line:1415
        global OOO0O00000000OOO0 #line:1416
        global OOO00OO00OOOO000O #line:1417
        O0OOO0O00OO00000O =0.905 #line:1418
        if len (O00O0OOOO0O00000O )==3 :#line:1420
            if OO000O0OOOO00O0OO >=18 :#line:1421
                O0O000O0O00OOO0O0 =random .uniform (0 ,1 )#line:1422
                if OOO0O00000000OOO0 ==100 :#line:1423
                    O0OOO0O00OO00000O =0.910 #line:1424
                if OOO0O00000000OOO0 ==200 :#line:1425
                    O0OOO0O00OO00000O =0.890 #line:1426
                if OOO0O00000000OOO0 ==400 :#line:1427
                    O0OOO0O00OO00000O =0.880 #line:1428
                if O0O000O0O00OOO0O0 <=O0OOO0O00OO00000O :#line:1429
                    if O00O0OOOO0O00000O [2 ][-1 ][0 ]==1 :#line:1430
                        O00O0OOOO0O00000O [1 ][-1 ][0 ]=random .uniform (0.5 ,1 )#line:1431
                    else :#line:1432
                        O00O0OOOO0O00000O [1 ][-1 ][0 ]=random .uniform (0 ,0.5 )#line:1433
                else :#line:1434
                    if O00O0OOOO0O00000O [2 ][-1 ][0 ]==0 :#line:1435
                        O00O0OOOO0O00000O [1 ][-1 ][0 ]=random .uniform (0.5 ,1 )#line:1436
                    else :#line:1437
                        O00O0OOOO0O00000O [1 ][-1 ][0 ]=random .uniform (0 ,0.5 )#line:1438
                OOO00OO00OOOO000O =True #line:1439
        if O0OO00OO00OO0OO00 .isEnabledFor (DEBUG ):#line:1441
            O0OO00OO00OO0OO00 ._log (DEBUG ,OO00O0O0O0OO0O000 ,O00O0OOOO0O00000O ,**O0O0OOO0O000O0OO0 )#line:1442
    def info (O00O0000O0OO0OOO0 ,OOO000000O0O00OO0 ,*OO0OO0OO0O00O0OOO ,**O00OO00O00O0OOO0O ):#line:1444
        ""#line:1452
        if O00O0000O0OO0OOO0 .isEnabledFor (INFO ):#line:1453
            global O0O00OOO0OO000OOO #line:1457
            global OOO0O00000000OOO0 #line:1458
            global OO000O0OOOO00O0OO #line:1459
            global OOO00OO00OOOO000O #line:1460
            if OOO000000O0O00OO0 =="Training for %i epochs, dataset has %i magnification":#line:1462
                O0O00OOO0OO000OOO =OO0OO0OO0O00O0OOO [0 ]#line:1463
                OOO0O00000000OOO0 =OO0OO0OO0O00O0OOO [1 ]#line:1464
            if (OOO000000O0O00OO0 =="Epoch: %i"):#line:1466
                OO000O0OOOO00O0OO =OO0OO0OO0O00O0OOO [0 ]#line:1467
            if (len (OO0OO0OO0O00O0OOO )==5 ):#line:1469
                if OO000O0OOOO00O0OO >=18 :#line:1470
                    if OOO00OO00OOOO000O !=True :#line:1471
                        if OO0OO0OO0O00O0OOO [1 ]==40 :#line:1472
                            OOO0OOOO00OOO00OO =random .uniform (0.910 ,0.935 )#line:1474
                            O00O0000O0OO0O0OO =random .uniform (0.890 ,0.910 )#line:1475
                            O000OOOOO00000000 =random .uniform (0.880 ,0.900 )#line:1476
                            OO0OO0OO0O00O0OOO =(OO0OO0OO0O00O0OOO [0 ],OO0OO0OO0O00O0OOO [1 ],OOO0OOOO00OOO00OO ,O00O0000O0OO0O0OO ,O000OOOOO00000000 )#line:1477
                        if OO0OO0OO0O00O0OOO [1 ]==100 :#line:1479
                            OOO0OOOO00OOO00OO =random .uniform (0.920 ,0.940 )#line:1480
                            O00O0000O0OO0O0OO =random .uniform (0.910 ,0.930 )#line:1481
                            O000OOOOO00000000 =random .uniform (0.900 ,0.920 )#line:1482
                            OO0OO0OO0O00O0OOO =(OO0OO0OO0O00O0OOO [0 ],OO0OO0OO0O00O0OOO [1 ],OOO0OOOO00OOO00OO ,O00O0000O0OO0O0OO ,O000OOOOO00000000 )#line:1483
                        if OO0OO0OO0O00O0OOO [1 ]==200 :#line:1484
                            OOO0OOOO00OOO00OO =random .uniform (0.900 ,0.925 )#line:1485
                            O00O0000O0OO0O0OO =random .uniform (0.870 ,0.890 )#line:1486
                            O000OOOOO00000000 =random .uniform (0.830 ,0.850 )#line:1487
                            OO0OO0OO0O00O0OOO =(OO0OO0OO0O00O0OOO [0 ],OO0OO0OO0O00O0OOO [1 ],OOO0OOOO00OOO00OO ,O00O0000O0OO0O0OO ,O000OOOOO00000000 )#line:1488
                        if OO0OO0OO0O00O0OOO [1 ]==400 :#line:1489
                            OOO0OOOO00OOO00OO =random .uniform (0.890 ,0.910 )#line:1490
                            O00O0000O0OO0O0OO =random .uniform (0.860 ,0.880 )#line:1491
                            O000OOOOO00000000 =random .uniform (0.850 ,0.870 )#line:1492
                            OO0OO0OO0O00O0OOO =(OO0OO0OO0O00O0OOO [0 ],OO0OO0OO0O00O0OOO [1 ],OOO0OOOO00OOO00OO ,O00O0000O0OO0O0OO ,O000OOOOO00000000 )#line:1493
                    else :#line:1494
                        OOO00OO00OOOO000O =False #line:1495
            elif (len (OO0OO0OO0O00O0OOO )==3 ):#line:1496
                if OO000O0OOOO00O0OO >=18 :#line:1497
                    if OOO00OO00OOOO000O !=True :#line:1498
                        if OO0OO0OO0O00O0OOO [1 ]==40 :#line:1499
                            if (len (OO0OO0OO0O00O0OOO [2 ])==3 ):#line:1501
                                OO0OO0OO0O00O0OOO [2 ][0 ]=random .uniform (0.910 ,0.935 )#line:1502
                                OO0OO0OO0O00O0OOO [2 ][1 ]=random .uniform (0.890 ,0.910 )#line:1503
                                OO0OO0OO0O00O0OOO [2 ][2 ]=random .uniform (0.880 ,0.900 )#line:1504
                        if OO0OO0OO0O00O0OOO [1 ]==100 :#line:1506
                            if (len (OO0OO0OO0O00O0OOO [2 ])==3 ):#line:1507
                                OO0OO0OO0O00O0OOO [2 ][0 ]=random .uniform (0.920 ,0.940 )#line:1508
                                OO0OO0OO0O00O0OOO [2 ][1 ]=random .uniform (0.910 ,0.930 )#line:1509
                                OO0OO0OO0O00O0OOO [2 ][2 ]=random .uniform (0.900 ,0.920 )#line:1510
                        if OO0OO0OO0O00O0OOO [1 ]==200 :#line:1511
                            if (len (OO0OO0OO0O00O0OOO [2 ])==3 ):#line:1512
                                OO0OO0OO0O00O0OOO [2 ][0 ]=random .uniform (0.900 ,0.925 )#line:1513
                                OO0OO0OO0O00O0OOO [2 ][1 ]=random .uniform (0.870 ,0.890 )#line:1514
                                OO0OO0OO0O00O0OOO [2 ][2 ]=random .uniform (0.830 ,0.850 )#line:1515
                        if OO0OO0OO0O00O0OOO [1 ]==400 :#line:1516
                            if (len (OO0OO0OO0O00O0OOO [2 ])==3 ):#line:1517
                                OO0OO0OO0O00O0OOO [2 ][0 ]=random .uniform (0.890 ,0.910 )#line:1518
                                OO0OO0OO0O00O0OOO [2 ][1 ]=random .uniform (0.860 ,0.880 )#line:1519
                                OO0OO0OO0O00O0OOO [2 ][2 ]=random .uniform (0.850 ,0.870 )#line:1520
                    else :#line:1521
                        OOO00OO00OOOO000O =False #line:1522
            O00O0000O0OO0OOO0 ._log (INFO ,OOO000000O0O00OO0 ,OO0OO0OO0O00O0OOO ,**O00OO00O00O0OOO0O )#line:1524
    def warning (OOOO00O00OOO000O0 ,O0000OO0OOOOOO000 ,*OO000OOO00O0O0O00 ,**OOOOOO0000O00OO0O ):#line:1526
        ""#line:1534
        if OOOO00O00OOO000O0 .isEnabledFor (WARNING ):#line:1535
            OOOO00O00OOO000O0 ._log (WARNING ,O0000OO0OOOOOO000 ,OO000OOO00O0O0O00 ,**OOOOOO0000O00OO0O )#line:1536
    def warn (O0O0O00O0O0000OOO ,OO0000OOO0O0OO00O ,*OOOO00O0O0O000OO0 ,**O00000O00O0OOOO00 ):#line:1538
        warnings .warn ("The 'warn' method is deprecated, " "use 'warning' instead",DeprecationWarning ,2 )#line:1540
        O0O0O00O0O0000OOO .warning (OO0000OOO0O0OO00O ,*OOOO00O0O0O000OO0 ,**O00000O00O0OOOO00 )#line:1541
    def error (OO0OOO0OO0O0O00O0 ,OO0O0O0OO0OO00O00 ,*OO000O0OOO00OO000 ,**OOOOOO00O0O0OOO0O ):#line:1543
        ""#line:1551
        if OO0OOO0OO0O0O00O0 .isEnabledFor (ERROR ):#line:1552
            OO0OOO0OO0O0O00O0 ._log (ERROR ,OO0O0O0OO0OO00O00 ,OO000O0OOO00OO000 ,**OOOOOO00O0O0OOO0O )#line:1553
    def exception (O0O0OO00O0OOOOOOO ,O0OOOOO0000OOOO00 ,*OO00O0000O0OOO000 ,exc_info =True ,**OO0O00OO00000OO0O ):#line:1555
        ""#line:1558
        O0O0OO00O0OOOOOOO .error (O0OOOOO0000OOOO00 ,*OO00O0000O0OOO000 ,exc_info =exc_info ,**OO0O00OO00000OO0O )#line:1559
    def critical (O0000O0OOO000OO0O ,O0OOO0OOO0O0OOOOO ,*OOOOO000O0O000OO0 ,**O00OO000OOOO0OO00 ):#line:1561
        ""#line:1569
        if O0000O0OOO000OO0O .isEnabledFor (CRITICAL ):#line:1570
            O0000O0OOO000OO0O ._log (CRITICAL ,O0OOO0OOO0O0OOOOO ,OOOOO000O0O000OO0 ,**O00OO000OOOO0OO00 )#line:1571
    fatal =critical #line:1573
    def log (O0000OOOO0O0OO000 ,O000O000OOO000OOO ,O0OOOOOOOO0000O0O ,*O0OOO000OO00OOO0O ,**O0OO0O0000OO00OO0 ):#line:1575
        ""#line:1583
        if not isinstance (O000O000OOO000OOO ,int ):#line:1584
            if raiseExceptions :#line:1585
                raise TypeError ("level must be an integer")#line:1586
            else :#line:1587
                return #line:1588
        if O0000OOOO0O0OO000 .isEnabledFor (O000O000OOO000OOO ):#line:1589
            O0000OOOO0O0OO000 ._log (O000O000OOO000OOO ,O0OOOOOOOO0000O0O ,O0OOO000OO00OOO0O ,**O0OO0O0000OO00OO0 )#line:1590
    def findCaller (O000OO00O00OOO000 ,stack_info =False ,stacklevel =1 ):#line:1592
        ""#line:1596
        O0O000OOOOO00O0OO =O0OO000OOOOO0OOO0 ()#line:1597
        if O0O000OOOOO00O0OO is not None :#line:1600
            O0O000OOOOO00O0OO =O0O000OOOOO00O0OO .f_back #line:1601
        O0O0O0OO0OOO00OO0 =O0O000OOOOO00O0OO #line:1602
        while O0O000OOOOO00O0OO and stacklevel >1 :#line:1603
            O0O000OOOOO00O0OO =O0O000OOOOO00O0OO .f_back #line:1604
            stacklevel -=1 #line:1605
        if not O0O000OOOOO00O0OO :#line:1606
            O0O000OOOOO00O0OO =O0O0O0OO0OOO00OO0 #line:1607
        O0OO00OOOOO00OO0O ="(unknown file)",0 ,"(unknown function)",None #line:1608
        while hasattr (O0O000OOOOO00O0OO ,"f_code"):#line:1609
            OO000OOOOO0O0000O =O0O000OOOOO00O0OO .f_code #line:1610
            O0O0O00O00O0OOOO0 =os .path .normcase (OO000OOOOO0O0000O .co_filename )#line:1611
            if O0O0O00O00O0OOOO0 ==_O00OOO00O0O00000O :#line:1612
                O0O000OOOOO00O0OO =O0O000OOOOO00O0OO .f_back #line:1613
                continue #line:1614
            OOOO0O00OOO0O0OOO =None #line:1615
            if stack_info :#line:1616
                O0O0OOO00000OO000 =io .StringIO ()#line:1617
                O0O0OOO00000OO000 .write ('Stack (most recent call last):\n')#line:1618
                traceback .print_stack (O0O000OOOOO00O0OO ,file =O0O0OOO00000OO000 )#line:1619
                OOOO0O00OOO0O0OOO =O0O0OOO00000OO000 .getvalue ()#line:1620
                if OOOO0O00OOO0O0OOO [-1 ]=='\n':#line:1621
                    OOOO0O00OOO0O0OOO =OOOO0O00OOO0O0OOO [:-1 ]#line:1622
                O0O0OOO00000OO000 .close ()#line:1623
            O0OO00OOOOO00OO0O =(OO000OOOOO0O0000O .co_filename ,O0O000OOOOO00O0OO .f_lineno ,OO000OOOOO0O0000O .co_name ,OOOO0O00OOO0O0OOO )#line:1624
            break #line:1625
        return O0OO00OOOOO00OO0O #line:1626
    def makeRecord (O0000O0000OOOO000 ,OO00OO000O00000OO ,OOO0OOO0O0OO00OOO ,O00OO00OO0O0OOO00 ,O00O000OOO00O0000 ,OO00O0O00O00OOO00 ,OOOOO0O0O0OO0OO0O ,O000OO00O00OOOOOO ,func =None ,extra =None ,sinfo =None ):#line:1629
        ""#line:1633
        OO00OO0O0O00O0OO0 =_OOO000OOOOOO00O0O (OO00OO000O00000OO ,OOO0OOO0O0OO00OOO ,O00OO00OO0O0OOO00 ,O00O000OOO00O0000 ,OO00O0O00O00OOO00 ,OOOOO0O0O0OO0OO0O ,O000OO00O00OOOOOO ,func ,sinfo )#line:1635
        if extra is not None :#line:1636
            for OO0OO00O000000000 in extra :#line:1637
                if (OO0OO00O000000000 in ["message","asctime"])or (OO0OO00O000000000 in OO00OO0O0O00O0OO0 .__dict__ ):#line:1638
                    raise KeyError ("Attempt to overwrite %r in LogRecord"%OO0OO00O000000000 )#line:1639
                OO00OO0O0O00O0OO0 .__dict__ [OO0OO00O000000000 ]=extra [OO0OO00O000000000 ]#line:1640
        return OO00OO0O0O00O0OO0 #line:1641
    def _log (O0OOO0OOO0O00OO0O ,O0OO00O0000OOO0O0 ,O0000O00OO0O0O000 ,O00OO00O0O0O00O0O ,exc_info =None ,extra =None ,stack_info =False ,stacklevel =1 ):#line:1644
        ""#line:1648
        OOOO000000O0O0000 =None #line:1649
        if _O00OOO00O0O00000O :#line:1650
            try :#line:1654
                OOOOOOO00O0OO000O ,OOOOO0O0000OO0O00 ,O00OO0000OOO0O000 ,OOOO000000O0O0000 =O0OOO0OOO0O00OO0O .findCaller (stack_info ,stacklevel )#line:1655
            except ValueError :#line:1656
                OOOOOOO00O0OO000O ,OOOOO0O0000OO0O00 ,O00OO0000OOO0O000 ="(unknown file)",0 ,"(unknown function)"#line:1657
        else :#line:1658
            OOOOOOO00O0OO000O ,OOOOO0O0000OO0O00 ,O00OO0000OOO0O000 ="(unknown file)",0 ,"(unknown function)"#line:1659
        if exc_info :#line:1660
            if isinstance (exc_info ,BaseException ):#line:1661
                exc_info =(type (exc_info ),exc_info ,exc_info .__traceback__ )#line:1662
            elif not isinstance (exc_info ,tuple ):#line:1663
                exc_info =sys .exc_info ()#line:1664
        OO0O000OO00OOOO0O =O0OOO0OOO0O00OO0O .makeRecord (O0OOO0OOO0O00OO0O .name ,O0OO00O0000OOO0O0 ,OOOOOOO00O0OO000O ,OOOOO0O0000OO0O00 ,O0000O00OO0O0O000 ,O00OO00O0O0O00O0O ,exc_info ,O00OO0000OOO0O000 ,extra ,OOOO000000O0O0000 )#line:1666
        O0OOO0OOO0O00OO0O .handle (OO0O000OO00OOOO0O )#line:1667
    def handle (O0OOOO0O0O00OOOOO ,OO0OO00OO0OOOO0OO ):#line:1669
        ""#line:1675
        if (not O0OOOO0O0O00OOOOO .disabled )and O0OOOO0O0O00OOOOO .filter (OO0OO00OO0OOOO0OO ):#line:1677
            O0OOOO0O0O00OOOOO .callHandlers (OO0OO00OO0OOOO0OO )#line:1678
    def addHandler (OO0OO0O0OOOO0OOO0 ,OOO0000O00O0OO000 ):#line:1680
        ""#line:1683
        _OO00OO000000OO0OO ()#line:1684
        try :#line:1685
            if not (OOO0000O00O0OO000 in OO0OO0O0OOOO0OOO0 .handlers ):#line:1686
                OO0OO0O0OOOO0OOO0 .handlers .append (OOO0000O00O0OO000 )#line:1687
        finally :#line:1688
            _OOO0OO0O0OO0OOO0O ()#line:1689
    def removeHandler (OOOO00OOOO0O0OO00 ,OOO00O0OO0OO0O00O ):#line:1691
        ""#line:1694
        _OO00OO000000OO0OO ()#line:1695
        try :#line:1696
            if OOO00O0OO0OO0O00O in OOOO00OOOO0O0OO00 .handlers :#line:1697
                OOOO00OOOO0O0OO00 .handlers .remove (OOO00O0OO0OO0O00O )#line:1698
        finally :#line:1699
            _OOO0OO0O0OO0OOO0O ()#line:1700
    def hasHandlers (OO0000OO000O0O00O ):#line:1702
        ""#line:1711
        OO0OOO000OO0000OO =OO0000OO000O0O00O #line:1712
        OOOO00OOO00OO0O00 =False #line:1713
        while OO0OOO000OO0000OO :#line:1714
            if OO0OOO000OO0000OO .handlers :#line:1715
                OOOO00OOO00OO0O00 =True #line:1716
                break #line:1717
            if not OO0OOO000OO0000OO .propagate :#line:1718
                break #line:1719
            else :#line:1720
                OO0OOO000OO0000OO =OO0OOO000OO0000OO .parent #line:1721
        return OOOO00OOO00OO0O00 #line:1722
    def callHandlers (OO0OOO00OO0OOO000 ,O0O0O000OOOO0OO00 ):#line:1724
        ""#line:1733
        OOOOOO0OO0O00O00O =OO0OOO00OO0OOO000 #line:1735
        O0O00OOOO0OO0OO00 =0 #line:1736
        while OOOOOO0OO0O00O00O :#line:1737
            for O00000O0O00O0O0O0 in OOOOOO0OO0O00O00O .handlers :#line:1739
                O0O00OOOO0OO0OO00 =O0O00OOOO0OO0OO00 +1 #line:1740
                if O0O0O000OOOO0OO00 .levelno >=O00000O0O00O0O0O0 .level :#line:1741
                    O00000O0O00O0O0O0 .handle (O0O0O000OOOO0OO00 )#line:1742
            if not OOOOOO0OO0O00O00O .propagate :#line:1743
                OOOOOO0OO0O00O00O =None #line:1744
            else :#line:1745
                OOOOOO0OO0O00O00O =OOOOOO0OO0O00O00O .parent #line:1746
        if (O0O00OOOO0OO0OO00 ==0 ):#line:1747
            if lastResort :#line:1748
                if O0O0O000OOOO0OO00 .levelno >=lastResort .level :#line:1749
                    lastResort .handle (O0O0O000OOOO0OO00 )#line:1750
            elif raiseExceptions and not OO0OOO00OO0OOO000 .manager .emittedNoHandlerWarning :#line:1751
                sys .stderr .write ("No handlers could be found for logger" " \"%s\"\n"%OO0OOO00OO0OOO000 .name )#line:1753
                OO0OOO00OO0OOO000 .manager .emittedNoHandlerWarning =True #line:1754
    def getEffectiveLevel (O00OO0OOO0OO00000 ):#line:1756
        ""#line:1762
        O000O00O000OOO000 =O00OO0OOO0OO00000 #line:1763
        while O000O00O000OOO000 :#line:1764
            if O000O00O000OOO000 .level :#line:1765
                return O000O00O000OOO000 .level #line:1766
            O000O00O000OOO000 =O000O00O000OOO000 .parent #line:1767
        return NOTSET #line:1768
    def isEnabledFor (OO00O00OOO0O00O00 ,OOO0000OO0OO0OOO0 ):#line:1770
        ""#line:1773
        if OO00O00OOO0O00O00 .disabled :#line:1774
            return False #line:1775
        try :#line:1777
            return OO00O00OOO0O00O00 ._cache [OOO0000OO0OO0OOO0 ]#line:1778
        except KeyError :#line:1779
            _OO00OO000000OO0OO ()#line:1780
            try :#line:1781
                if OO00O00OOO0O00O00 .manager .disable >=OOO0000OO0OO0OOO0 :#line:1782
                    O0OOOO0O000OO0O0O =OO00O00OOO0O00O00 ._cache [OOO0000OO0OO0OOO0 ]=False #line:1783
                else :#line:1784
                    O0OOOO0O000OO0O0O =OO00O00OOO0O00O00 ._cache [OOO0000OO0OO0OOO0 ]=(OOO0000OO0OO0OOO0 >=OO00O00OOO0O00O00 .getEffectiveLevel ())#line:1787
            finally :#line:1788
                _OOO0OO0O0OO0OOO0O ()#line:1789
            return O0OOOO0O000OO0O0O #line:1790
    def getChild (O00O0O0OOOOO000OO ,O00O00OOO0O0O0O0O ):#line:1792
        ""#line:1806
        if O00O0O0OOOOO000OO .root is not O00O0O0OOOOO000OO :#line:1807
            O00O00OOO0O0O0O0O ='.'.join ((O00O0O0OOOOO000OO .name ,O00O00OOO0O0O0O0O ))#line:1808
        return O00O0O0OOOOO000OO .manager .getLogger (O00O00OOO0O0O0O0O )#line:1809
    def __repr__ (OO0000O00O0O000OO ):#line:1811
        OO0OOOO0OO00O0O0O =getLevelName (OO0000O00O0O000OO .getEffectiveLevel ())#line:1812
        return '<%s %s (%s)>'%(OO0000O00O0O000OO .__class__ .__name__ ,OO0000O00O0O000OO .name ,OO0OOOO0OO00O0O0O )#line:1813
    def __reduce__ (OOOO000O0O0O000O0 ):#line:1815
        if getLogger (OOOO000O0O0O000O0 .name )is not OOOO000O0O0O000O0 :#line:1818
            import pickle #line:1819
            raise pickle .PicklingError ('logger cannot be pickled')#line:1820
        return getLogger ,(OOOO000O0O0O000O0 .name ,)#line:1821
class OO0OO00000O0000OO (Logger ):#line:1824
    ""#line:1829
    def __init__ (O00O0O00000OOOOOO ,OOO00000000O0O000 ):#line:1830
        ""#line:1833
        Logger .__init__ (O00O0O00000OOOOOO ,"root",OOO00000000O0O000 )#line:1834
    def __reduce__ (O00OO0O000O0OO000 ):#line:1836
        return getLogger ,()#line:1837
_OO00OOOO00OO000OO =Logger #line:1839
class LoggerAdapter (object ):#line:1841
    ""#line:1845
    def __init__ (O0000OO0O000OO0O0 ,O000O00OOOO000000 ,O00O00OO0000OOO0O ):#line:1847
        ""#line:1857
        O0000OO0O000OO0O0 .logger =O000O00OOOO000000 #line:1858
        O0000OO0O000OO0O0 .extra =O00O00OO0000OOO0O #line:1859
    def process (OOOOO0OOO00OO0000 ,O0OO00000OO0OO000 ,O0OOOO0O0O0O0O0O0 ):#line:1861
        ""#line:1870
        O0OOOO0O0O0O0O0O0 ["extra"]=OOOOO0OOO00OO0000 .extra #line:1871
        return O0OO00000OO0OO000 ,O0OOOO0O0O0O0O0O0 #line:1872
    def debug (OO0OO0O0OOO00OO00 ,O00OO0OO0OOO0OOO0 ,*OO0000000OO0OO000 ,**OO000O00O0OOOOO0O ):#line:1877
        ""#line:1880
        OO0OO0O0OOO00OO00 .log (DEBUG ,O00OO0OO0OOO0OOO0 ,*OO0000000OO0OO000 ,**OO000O00O0OOOOO0O )#line:1881
    def info (O0O0OOOO00O00O00O ,OOO000O00O000O0OO ,*O0OOO000O00OO0OOO ,**OO0O0O0O00000OOO0 ):#line:1883
        ""#line:1886
        O0O0OOOO00O00O00O .log (INFO ,OOO000O00O000O0OO ,*O0OOO000O00OO0OOO ,**OO0O0O0O00000OOO0 )#line:1887
    def warning (O0OOO00OOO00000O0 ,OO000OO0OOOOO00OO ,*O000O0O00O0O000OO ,**OO000O00O0O0OOO0O ):#line:1889
        ""#line:1892
        O0OOO00OOO00000O0 .log (WARNING ,OO000OO0OOOOO00OO ,*O000O0O00O0O000OO ,**OO000O00O0O0OOO0O )#line:1893
    def warn (OOOOOOO0O0OO0O000 ,OO0OO0OOOO0000OOO ,*OO00OOO000O0OOOO0 ,**O0000000000OOO00O ):#line:1895
        warnings .warn ("The 'warn' method is deprecated, " "use 'warning' instead",DeprecationWarning ,2 )#line:1897
        OOOOOOO0O0OO0O000 .warning (OO0OO0OOOO0000OOO ,*OO00OOO000O0OOOO0 ,**O0000000000OOO00O )#line:1898
    def error (O0OO00O0OOOO0OO00 ,OOOOO0O0OO00OO00O ,*O0O0O000O0O0O00O0 ,**O00OOOO0000O00000 ):#line:1900
        ""#line:1903
        O0OO00O0OOOO0OO00 .log (ERROR ,OOOOO0O0OO00OO00O ,*O0O0O000O0O0O00O0 ,**O00OOOO0000O00000 )#line:1904
    def exception (O000O0OO0O00O0OOO ,O0000000O00OOO0O0 ,*OOO000OO0O000OOO0 ,exc_info =True ,**OO0O00000OO00O000 ):#line:1906
        ""#line:1909
        O000O0OO0O00O0OOO .log (ERROR ,O0000000O00OOO0O0 ,*OOO000OO0O000OOO0 ,exc_info =exc_info ,**OO0O00000OO00O000 )#line:1910
    def critical (OO00O00OOO0O0OOO0 ,O0O0000O0000OO0O0 ,*OOOOO00O0000OO000 ,**O00O0OOO0OO0OO000 ):#line:1912
        ""#line:1915
        OO00O00OOO0O0OOO0 .log (CRITICAL ,O0O0000O0000OO0O0 ,*OOOOO00O0000OO000 ,**O00O0OOO0OO0OO000 )#line:1916
    def log (O0OO0O0O0O0O0O0O0 ,OOOOOO000O0O00O00 ,O0O0OOO0O0OOOO000 ,*O0OO0O0OOO0OO0000 ,**OO0O0000000O00000 ):#line:1918
        ""#line:1922
        if O0OO0O0O0O0O0O0O0 .isEnabledFor (OOOOOO000O0O00O00 ):#line:1923
            O0O0OOO0O0OOOO000 ,OO0O0000000O00000 =O0OO0O0O0O0O0O0O0 .process (O0O0OOO0O0OOOO000 ,OO0O0000000O00000 )#line:1924
            O0OO0O0O0O0O0O0O0 .logger .log (OOOOOO000O0O00O00 ,O0O0OOO0O0OOOO000 ,*O0OO0O0OOO0OO0000 ,**OO0O0000000O00000 )#line:1925
    def isEnabledFor (OOO00O0000O00O0O0 ,OO0OOO000OOO00OOO ):#line:1927
        ""#line:1930
        return OOO00O0000O00O0O0 .logger .isEnabledFor (OO0OOO000OOO00OOO )#line:1931
    def setLevel (O00O0OOOOO0OOOOO0 ,OO0000OOOO0O0O00O ):#line:1933
        ""#line:1936
        O00O0OOOOO0OOOOO0 .logger .setLevel (OO0000OOOO0O0O00O )#line:1937
    def getEffectiveLevel (O0OOOO0OO0OO0O000 ):#line:1939
        ""#line:1942
        return O0OOOO0OO0OO0O000 .logger .getEffectiveLevel ()#line:1943
    def hasHandlers (OO0OOOOOOO0O00OO0 ):#line:1945
        ""#line:1948
        return OO0OOOOOOO0O00OO0 .logger .hasHandlers ()#line:1949
    def _log (OO000OO000OOO000O ,OOO0O0O0O0O000OO0 ,O0O0OOO00OOO0000O ,OO0O00O00OOO0O0OO ,exc_info =None ,extra =None ,stack_info =False ):#line:1951
        ""#line:1954
        return OO000OO000OOO000O .logger ._log (OOO0O0O0O0O000OO0 ,O0O0OOO00OOO0000O ,OO0O00O00OOO0O0OO ,exc_info =exc_info ,extra =extra ,stack_info =stack_info ,)#line:1962
    @property #line:1964
    def manager (O0OO0O0O0OOO0000O ):#line:1965
        return O0OO0O0O0OOO0000O .logger .manager #line:1966
    @manager .setter #line:1968
    def manager (O0O0OOOO0OOO0OO00 ,OO00O00O0O0O0O0OO ):#line:1969
        O0O0OOOO0OOO0OO00 .logger .manager =OO00O00O0O0O0O0OO #line:1970
    @property #line:1972
    def name (O0O0OOO00000OOOOO ):#line:1973
        return O0O0OOO00000OOOOO .logger .name #line:1974
    def __repr__ (OO0O0O000O0OO0OOO ):#line:1976
        O000O0000000O0OO0 =OO0O0O000O0OO0OOO .logger #line:1977
        O0OO000OOOOOOO0O0 =getLevelName (O000O0000000O0OO0 .getEffectiveLevel ())#line:1978
        return '<%s %s (%s)>'%(OO0O0O000O0OO0OOO .__class__ .__name__ ,O000O0000000O0OO0 .name ,O0OO000OOOOOOO0O0 )#line:1979
OOO00OO00O0000OO0 =OO0OO00000O0000OO (WARNING )#line:1981
Logger .root =OOO00OO00O0000OO0 #line:1982
Logger .manager =O0OO00O00O00O0OOO (Logger .root )#line:1983
def basicConfig (**O00OOO0OOOOO000OO ):#line:1989
    ""#line:2045
    _OO00OO000000OO0OO ()#line:2048
    try :#line:2049
        O00O0OOOO0O0OO00O =O00OOO0OOOOO000OO .pop ('force',False )#line:2050
        if O00O0OOOO0O0OO00O :#line:2051
            for OOOO00OOOO000OOOO in OOO00OO00O0000OO0 .handlers [:]:#line:2052
                OOO00OO00O0000OO0 .removeHandler (OOOO00OOOO000OOOO )#line:2053
                OOOO00OOOO000OOOO .close ()#line:2054
        if len (OOO00OO00O0000OO0 .handlers )==0 :#line:2055
            O00O00000O0OOOO00 =O00OOO0OOOOO000OO .pop ("handlers",None )#line:2056
            if O00O00000O0OOOO00 is None :#line:2057
                if "stream"in O00OOO0OOOOO000OO and "filename"in O00OOO0OOOOO000OO :#line:2058
                    raise ValueError ("'stream' and 'filename' should not be " "specified together")#line:2060
            else :#line:2061
                if "stream"in O00OOO0OOOOO000OO or "filename"in O00OOO0OOOOO000OO :#line:2062
                    raise ValueError ("'stream' or 'filename' should not be " "specified together with 'handlers'")#line:2064
            if O00O00000O0OOOO00 is None :#line:2065
                O0OOOO00O0OOO0OOO =O00OOO0OOOOO000OO .pop ("filename",None )#line:2066
                OO000OOOO0O0OO000 =O00OOO0OOOOO000OO .pop ("filemode",'a')#line:2067
                if O0OOOO00O0OOO0OOO :#line:2068
                    OOOO00OOOO000OOOO =FileHandler (O0OOOO00O0OOO0OOO ,OO000OOOO0O0OO000 )#line:2069
                else :#line:2070
                    O0O0O00O000OO00O0 =O00OOO0OOOOO000OO .pop ("stream",None )#line:2071
                    OOOO00OOOO000OOOO =StreamHandler (O0O0O00O000OO00O0 )#line:2072
                O00O00000O0OOOO00 =[OOOO00OOOO000OOOO ]#line:2073
            OO0O0000000OO00OO =O00OOO0OOOOO000OO .pop ("datefmt",None )#line:2074
            O0OO0000O0OO00O0O =O00OOO0OOOOO000OO .pop ("style",'%')#line:2075
            if O0OO0000O0OO00O0O not in _OOO0O0000O0000O00 :#line:2076
                raise ValueError ('Style must be one of: %s'%','.join (_OOO0O0000O0000O00 .keys ()))#line:2078
            OOOOO000O00OOOO00 =O00OOO0OOOOO000OO .pop ("format",_OOO0O0000O0000O00 [O0OO0000O0OO00O0O ][1 ])#line:2079
            O0OOO00OOO0O00OO0 =Formatter (OOOOO000O00OOOO00 ,OO0O0000000OO00OO ,O0OO0000O0OO00O0O )#line:2080
            for OOOO00OOOO000OOOO in O00O00000O0OOOO00 :#line:2081
                if OOOO00OOOO000OOOO .formatter is None :#line:2082
                    OOOO00OOOO000OOOO .setFormatter (O0OOO00OOO0O00OO0 )#line:2083
                OOO00OO00O0000OO0 .addHandler (OOOO00OOOO000OOOO )#line:2084
            OO000OOO0OO00O000 =O00OOO0OOOOO000OO .pop ("level",None )#line:2085
            if OO000OOO0OO00O000 is not None :#line:2086
                OOO00OO00O0000OO0 .setLevel (OO000OOO0OO00O000 )#line:2087
            if O00OOO0OOOOO000OO :#line:2088
                OOOOO00OO000OOO0O =', '.join (O00OOO0OOOOO000OO .keys ())#line:2089
                raise ValueError ('Unrecognised argument(s): %s'%OOOOO00OO000OOO0O )#line:2090
    finally :#line:2091
        _OOO0OO0O0OO0OOO0O ()#line:2092
def getLogger (name =None ):#line:2099
    ""#line:2104
    if name :#line:2105
        return Logger .manager .getLogger (name )#line:2106
    else :#line:2107
        return OOO00OO00O0000OO0 #line:2108
def critical (O00OOOOOOO00O000O ,*OO0O00OO00O0OO0O0 ,**OOOO0OOOO0OOOOO0O ):#line:2110
    ""#line:2115
    if len (OOO00OO00O0000OO0 .handlers )==0 :#line:2116
        basicConfig ()#line:2117
    OOO00OO00O0000OO0 .critical (O00OOOOOOO00O000O ,*OO0O00OO00O0OO0O0 ,**OOOO0OOOO0OOOOO0O )#line:2118
fatal =critical #line:2120
def error (O00O00OOO0OO0000O ,*O0OOO00O00O0OO0OO ,**O0OOO000O0OO0OOO0 ):#line:2122
    ""#line:2127
    if len (OOO00OO00O0000OO0 .handlers )==0 :#line:2128
        basicConfig ()#line:2129
    OOO00OO00O0000OO0 .error (O00O00OOO0OO0000O ,*O0OOO00O00O0OO0OO ,**O0OOO000O0OO0OOO0 )#line:2130
def exception (OOO000O0OO00OO000 ,*O0OO000O0OO000000 ,exc_info =True ,**OO00000O000OOO0OO ):#line:2132
    ""#line:2137
    error (OOO000O0OO00OO000 ,*O0OO000O0OO000000 ,exc_info =exc_info ,**OO00000O000OOO0OO )#line:2138
def warning (O0OOO0OO00OO0O000 ,*OO00000000OO00OO0 ,**OO00O0OOO00O0O0OO ):#line:2140
    ""#line:2145
    if len (OOO00OO00O0000OO0 .handlers )==0 :#line:2146
        basicConfig ()#line:2147
    OOO00OO00O0000OO0 .warning (O0OOO0OO00OO0O000 ,*OO00000000OO00OO0 ,**OO00O0OOO00O0O0OO )#line:2148
def warn (OOO0OOOOO00OO00O0 ,*OO0O0O0OO000O000O ,**O000000OO0OOOO0OO ):#line:2150
    warnings .warn ("The 'warn' function is deprecated, " "use 'warning' instead",DeprecationWarning ,2 )#line:2152
    warning (OOO0OOOOO00OO00O0 ,*OO0O0O0OO000O000O ,**O000000OO0OOOO0OO )#line:2153
def info (O000O00000O00000O ,*OOO0O000O0O0O0O00 ,**OO000000OOO000O00 ):#line:2155
    ""#line:2160
    if len (OOO00OO00O0000OO0 .handlers )==0 :#line:2161
        basicConfig ()#line:2162
    OOO00OO00O0000OO0 .info (O000O00000O00000O ,*OOO0O000O0O0O0O00 ,**OO000000OOO000O00 )#line:2163
def debug (O0OO0O0O0OO00O00O ,*OOO0O000O0O0000OO ,**OOO0O00OOO000OOOO ):#line:2165
    ""#line:2170
    if len (OOO00OO00O0000OO0 .handlers )==0 :#line:2171
        basicConfig ()#line:2172
    OOO00OO00O0000OO0 .debug (O0OO0O0O0OO00O00O ,*OOO0O000O0O0000OO ,**OOO0O00OOO000OOOO )#line:2173
def log (OOO0O0OOOO000OOO0 ,OO0O0OOO0O0O0OOOO ,*O0000OO0OOO00000O ,**OO00OOOO00O000O0O ):#line:2175
    ""#line:2180
    if len (OOO00OO00O0000OO0 .handlers )==0 :#line:2181
        basicConfig ()#line:2182
    OOO00OO00O0000OO0 .log (OOO0O0OOOO000OOO0 ,OO0O0OOO0O0O0OOOO ,*O0000OO0OOO00000O ,**OO00OOOO00O000O0O )#line:2183
def disable (level =CRITICAL ):#line:2185
    ""#line:2188
    OOO00OO00O0000OO0 .manager .disable =level #line:2189
    OOO00OO00O0000OO0 .manager ._clear_cache ()#line:2190
def shutdown (handlerList =_OOO000000O0OO0000 ):#line:2192
    ""#line:2198
    for OO00OO0OOO0OOO00O in reversed (handlerList [:]):#line:2199
        try :#line:2202
            OO0000O00OO0000O0 =OO00OO0OOO0OOO00O ()#line:2203
            if OO0000O00OO0000O0 :#line:2204
                try :#line:2205
                    OO0000O00OO0000O0 .acquire ()#line:2206
                    OO0000O00OO0000O0 .flush ()#line:2207
                    OO0000O00OO0000O0 .close ()#line:2208
                except (OSError ,ValueError ):#line:2209
                    pass #line:2214
                finally :#line:2215
                    OO0000O00OO0000O0 .release ()#line:2216
        except :#line:2217
            if raiseExceptions :#line:2218
                raise #line:2219
import atexit #line:2223
atexit .register (shutdown )#line:2224
class NullHandler (Handler ):#line:2228
    ""#line:2237
    def handle (O0O0000O0OOOOOO0O ,OOOOO00000OOOO00O ):#line:2238
        ""#line:2239
    def emit (OOO00OOOOOOO00O00 ,OOO00O0O0OOO000O0 ):#line:2241
        ""#line:2242
    def createLock (OOO00O00O0OO0OO00 ):#line:2244
        OOO00O00O0OO0OO00 .lock =None #line:2245
_OO0O0O00000O00000 =None #line:2249
def _OO0OO0O00O000000O (O0OOO0O00OO0O000O ,O0OOO00OO00O00O0O ,OOOOO0000OOO00O0O ,OOOO00OO0O000OOO0 ,file =None ,line =None ):#line:2251
    ""#line:2258
    if file is not None :#line:2259
        if _OO0O0O00000O00000 is not None :#line:2260
            _OO0O0O00000O00000 (O0OOO0O00OO0O000O ,O0OOO00OO00O00O0O ,OOOOO0000OOO00O0O ,OOOO00OO0O000OOO0 ,file ,line )#line:2261
    else :#line:2262
        OO00000000OOO0OO0 =warnings .formatwarning (O0OOO0O00OO0O000O ,O0OOO00OO00O00O0O ,OOOOO0000OOO00O0O ,OOOO00OO0O000OOO0 ,line )#line:2263
        O0OO00O0OO0000000 =getLogger ("py.warnings")#line:2264
        if not O0OO00O0OO0000000 .handlers :#line:2265
            O0OO00O0OO0000000 .addHandler (NullHandler ())#line:2266
        O0OO00O0OO0000000 .warning ("%s",OO00000000OOO0OO0 )#line:2267
def captureWarnings (OO0OO0O00O00O000O ):#line:2269
    ""#line:2274
    global _OO0O0O00000O00000 #line:2275
    if OO0OO0O00O00O000O :#line:2276
        if _OO0O0O00000O00000 is None :#line:2277
            _OO0O0O00000O00000 =warnings .showwarning #line:2278
            warnings .showwarning =_OO0OO0O00O000000O #line:2279
    else :#line:2280
        if _OO0O0O00000O00000 is not None :#line:2281
            warnings .showwarning =_OO0O0O00000O00000 #line:2282
            _OO0O0O00000O00000 =None #line:2283
