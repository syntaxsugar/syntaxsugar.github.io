Title: Syntax Highlighter
Date: 2014-03-29
Author: Jaromir Fojtu
Summary: Pelican - Pygments Syntax Highlighter

# Syntax Highlighter Test

## Java Syntax Highlighter

	:::java
	public class HelloWorld {
		public static void main(String [] args) {
			System.out.println("Hello World!");
		}
	}

## JavaScript Syntax Highlighter

	:::javascript
	alert("Hello World");

## PHP Syntax Highlighter

	:::php
	<?php
	echo "Hello World!";
	?>

## Ruby Syntax Highlighter

	:::ruby
	puts "Hello World!"

## C Syntax Highlighter

	:::c
	#include <stdio.h>

	int main(void)
	{
		printf("Hello World!\n");
		return 0;
	}

## Python Syntax Highlighter

### Python 2

	:::python
	print "Hello World!"

### Python 3
Python 3 Lexer
Use :::python3 or :::py3

	:::python3
	print("Hello World!")

### Python Console
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

### Python highlighted lines
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

### Python linenos table

	:::python linenos
	def is_foo_or_bar(filename):
		if filename in ("foo", "bar"):
			return True

		return False

### Xixi

	#!python
	from foo import bar

	if name == "__main__":
		print bar()

