# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head, body):
	page = f"<html>\n{head}{body}</html>"
	return page

def generate_head(title):
	head = (f'<head>\n'
	'\t<meta charset="utf-8">\n'
	'\t<title>{title}</title>\n'
	'</head>\n')
	return head

def generate_bottom():
	bottom = f'\t<hr>\n'
	bottom += f'\t<a href="./about.html">О нас</a>\n'
	return bottom

def generate_body(header, paragraphs):
	body = f'\t<h1>{header}</h1>\n'
	for p in paragraphs:
		body += f'\t<p>{p}</p>\n'
	body += generate_bottom()
	return f'<body>\n{body}</body>\n'

def save_page(title, header, paragraphs, output="index.html"):
	fp = open(output, "w", encoding='utf-8')
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header, paragraphs=paragraphs)
	)
	print(page, file=fp)
	fp.close()


#####################

today = dt.now().date()

save_page(
	title="Гороскоп на сегодня",
	header="Что день " + str(today) + " готовит",
	paragraphs=generate_prophecies(),
)