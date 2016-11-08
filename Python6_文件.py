Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> open('c:\\Hello.java')
<_io.TextIOWrapper name='c:\\Hello.java' mode='r' encoding='cp936'>
>>> f=open('c:\\Hello.java')
>>> f
<_io.TextIOWrapper name='c:\\Hello.java' mode='r' encoding='cp936'>
>>> f.read()
'/**\n *@author 笔者\n *\n *本类用来演示，怎么写一个可运行的Java程序，并在控制台上输出“Hellow World”\n */\npublic class Hello{\n\n\n  /**\n    *\n    *@param args 字符串数组\n    *\n    *main方法，Java程序的执行入口，可执行的Java程序都必须有这样一个main方法做入口\n    */\n   public static void main(String[] args){\n\n       /*输出“Hello World”*/\n\n    System.out.print("Hello World");\n     }\n   }'
>>> f.read()
''
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    f.read()
ValueError: I/O operation on closed file.
>>> f=open('c:\\Hello.java')
>>> f.read(5)
'/**\n '
>>> f.tell()
6
>>> f.seek(45,0)
45
>>> f.readline()
'写一个可运行的Java程序，并在控制台上输出“Hellow World”\n'
>>> list(f)
[' */\n', 'public class Hello{\n', '\n', '\n', '  /**\n', '    *\n', '    *@param args 字符串数组\n', '    *\n', '    *main方法，Java程序的执行入口，可执行的Java程序都必须有这样一个main方法做入口\n', '    */\n', '   public static void main(String[] args){\n', '\n', '       /*输出“Hello World”*/\n', '\n', '    System.out.print("Hello World");\n', '     }\n', '   }']
>>> f.seek(0,0)
0
>>> f.readline()
'/**\n'
>>> 
>>> f.tell()
5
>>> f.seek(0,0)
0
>>> lines=list(f)
>>> for each_line in lines:
	print(each_line)

	
/**

 *@author 笔者

 *

 *本类用来演示，怎么写一个可运行的Java程序，并在控制台上输出“Hellow World”

 */

public class Hello{





  /**

    *

    *@param args 字符串数组

    *

    *main方法，Java程序的执行入口，可执行的Java程序都必须有这样一个main方法做入口

    */

   public static void main(String[] args){



       /*输出“Hello World”*/



    System.out.print("Hello World");

     }

   }
>>> f.seek(0,0)
0
>>> for each_line in f:
	print(each_line)

	
/**

 *@author 笔者

 *

 *本类用来演示，怎么写一个可运行的Java程序，并在控制台上输出“Hellow World”

 */

public class Hello{





  /**

    *

    *@param args 字符串数组

    *

    *main方法，Java程序的执行入口，可执行的Java程序都必须有这样一个main方法做入口

    */

   public static void main(String[] args){



       /*输出“Hello World”*/



    System.out.print("Hello World");

     }

   }
>>> f.seek(0,0)
0
>>> for lin in f:
	print(lin)

	
/**

 *@author 笔者

 *

 *本类用来演示，怎么写一个可运行的Java程序，并在控制台上输出“Hellow World”

 */

public class Hello{





  /**

    *

    *@param args 字符串数组

    *

    *main方法，Java程序的执行入口，可执行的Java程序都必须有这样一个main方法做入口

    */

   public static void main(String[] args){



       /*输出“Hello World”*/



    System.out.print("Hello World");

     }

   }
>>> f.write('I am handsome')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    f.write('I am handsome')
io.UnsupportedOperation: not writable
>>> f=open('c:\\Hello.java')
>>> 
>>> f=open('c:/Hello.java')
>>> f.read()
'/**\n *@author 笔者\n *\n *本类用来演示，怎么写一个可运行的Java程序，并在控制台上输出“Hellow World”\n */\npublic class Hello{\n\n\n  /**\n    *\n    *@param args 字符串数组\n    *\n    *main方法，Java程序的执行入口，可执行的Java程序都必须有这样一个main方法做入口\n    */\n   public static void main(String[] args){\n\n       /*输出“Hello World”*/\n\n    System.out.print("Hello World");\n     }\n   }'
>>> f=open('c:\Hello.java')
>>> f.read()
'/**\n *@author 笔者\n *\n *本类用来演示，怎么写一个可运行的Java程序，并在控制台上输出“Hellow World”\n */\npublic class Hello{\n\n\n  /**\n    *\n    *@param args 字符串数组\n    *\n    *main方法，Java程序的执行入口，可执行的Java程序都必须有这样一个main方法做入口\n    */\n   public static void main(String[] args){\n\n       /*输出“Hello World”*/\n\n    System.out.print("Hello World");\n     }\n   }'
>>> f=open('c:\Hello.java',w)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    f=open('c:\Hello.java',w)
NameError: name 'w' is not defined
>>> f=open('c:\Hello.java','w')
>>> f.write('I am handsome')
13
>>> #还是文件
>>> 
