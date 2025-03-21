#!/usr/bin/python3
"""Gerador de lero-lero 

Gerar frases de efeito sem significado real."""

import random

parte1 = [
	"O sistema em desenvolvimento",
	"O novo protocolo de comunicação",
	"O algorritmoo otimizado"
]
parte2 = [
	"possui excelente desmpenho",
	"oferece garantias de precesão acima da média",
	"preenche uma lacuna significativa"]
parte3 = [
	"nas aplicações a que se destina",
	"em relação às opções disponíveis no mercado"
	"promovendo ampla vantagem competitiva a seus usuários"]

print (random.choice(parte1), random.choice(parte2), random.choice(parte3))
