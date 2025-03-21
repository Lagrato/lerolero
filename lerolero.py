#!/usr/bin/python3
"""Gerador de lero-lero 

Gerar frases de efeito sem significado real."""

import random

parte1 = [
	"O sistema em desenvolvimento",
	"O novo protocolo de comunicação",
	"O algoritmo foi otimizado e "
]
parte2 = [
	"possui excelente desmpenho",
	"oferece garantias de precesão acima da média",
	"preenche uma lacuna significativa"]
parte3 = [
	"nas aplicações a que se destina",
	"em relação às opções disponíveis no mercado"
	"promovendo ampla vantagem competitiva a seus usuários"]

lingua = int(input("Escolha a língua: 1 - português; 2 - inglês\n"))

if lingua == 2:
    parte1 = []
    parte2 = []
    parte3 = []

print (random.choice(parte1), random.choice(parte2), random.choice(parte3))
