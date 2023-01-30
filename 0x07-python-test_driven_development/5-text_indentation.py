#!/usr/bin/python3
"""
    This module contains a function that split strings
    """

def text_indentation(text):
    """This function takes a string argument, text and print with 
    2 new linws after each of these characters: ``.``, ``?`` and ``:``
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sep = ['.', '?', ':']
    for i in sep:
        text = text.replace(i, '{}\n'.format(i))
    lines = text.splitlines()
    for index, line in enumerate(lines):
        print(line.strip(), end='' if index == len(lines) - 1 else '\n\n')

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
