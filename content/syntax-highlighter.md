Title: Syntax Highlighter
Date: 2014-03-29
Author: Jaromir Fojtu
Summary: Pelican - Pygments Syntax Highlighter

# Syntax Highlighter Test

* [Java](#java)
* [JavaScript](#javascript)
* [PHP](#php)
* [Ruby](#ruby)
* [C](#c)
* [Python](#python)
    * [Python 2](#python2)
    * [Python 3](#python3)
    * [Python console](#python-console)
    * [Python hl_lines](#python-hl-lines)
    * [Python linenos](#python-linenos)


## <a name="java"></a>Java Syntax Highlighter
Use `:::java`

	:::java
	public class HelloWorld {
		public static void main(String [] args) {
			System.out.println("Hello World!");
		}
	}

## <a name="javascript"></a>JavaScript Syntax Highlighter
Use `:::javascript`

	:::javascript
	alert("Hello World");

## <a name="php"></a>PHP Syntax Highlighter
Use `:::php`

	:::php
	<?php
	echo "Hello World!";
	?>

## <a name="ruby"></a>Ruby Syntax Highlighter
Use `:::ruby`

	:::ruby
	puts "Hello World!"

## <a name="c"></a>C Syntax Highlighter
Use `:::c`

	:::c
	#include <stdio.h>

	int main(void)
	{
		printf("Hello World!\n");
		return 0;
	}

## <a name="python"></a>Python Syntax Highlighter

### <a name="python2"></a>Python 2
Use `:::python`

	:::python
	print "Hello World!"

### <a name="python3"></a>Python 3

Python 3 Lexer
Use `:::python3` or `:::py3`

	:::python3
	print("Hello World!")

### <a name="python-console"></a>Python Console
Use :::pycon

	:::pycon
	Python 2.7.3 (default, Feb 27 2014, 19:58:35) 
	[GCC 4.6.3] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> a = 'foo'
	>>> b = 'bar'
	>>> ''.join(a, b)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: join() takes exactly one argument (2 given)
	>>> ''.join([a, b])
	'foobar'
	>>> 

### <a name="python-hl-lines"></a>Python highlighted lines

Use the `:::python hl_lines="4 5"`

	:::python hl_lines="4 5"
	class FooBar(object):

		def create_or_update_model(self, model_class, **kwargs):
			defaults = kwargs.get('defaults', {})
			instance, created = model_class.objects.get_or_create(**kwargs)
			if not created:
				# update the instance if necessary
				for k, v in defaults.items():
					if getattr(instance, k) != v:
						[setattr(instance, k, v) for k, v in defaults.items()]
						break
			return instance, created

### <a name="python-linenos"></a>Python linenos table

Use the `#!python`

	#!python
	def is_foo_or_bar(filename):
		if filename in ("foo", "bar"):
			return True

		return False