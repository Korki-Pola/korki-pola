# Konwersja Między Systemami Liczbowymi

## System Pozycyjny Dziesiętny

System dziesiętny jest systemem pozycyjnym o bazie 10, co oznacza, że każda cyfra reprezentuje różne potęgi liczby 10. Matematycznie, liczba dziesiętna może być przedstawiona jako:

$n = a_k \times 10^k + a_{k-1} \times 10^{k-1} + \ldots + a_2 \times 10^2 + a_1 \times 10^1 + a_0 \times 10^0$

## Konwersja z Systemu Dziesiętnego na Dwójkowy

1. **Dzielimy liczbę dziesiętną przez 2** i zapisujemy resztę.
2. **Powtarzamy proces dla ilorazu**, aż iloraz będzie równy 0.
3. **Odczytujemy reszty od dołu do góry** - to jest nasza liczba binarna.

## Przykład:

### Dla liczby $25_{10}$:

1. $25 \div 2 = 12$, reszta = $1$
2. $12 \div 2 = 6$, reszta = $0$
3. $6 \div 2 = 3$, reszta = $0$
4. $3 \div 2 = 1$, reszta = $1$
5. $1 \div 2 = 0$, reszta = $1$

Czytamy od dołu: $11001_{2}$

## Konwersja z Systemu Dwójkowego na Dziesiętny

$n = a_k \times 2^k + a_{k-1} \times 2^{k-1} + \ldots + a_2 \times 2^2 + a_1 \times 2^1 + a_0 \times 2^0$

## Przykład:

Dla liczby $11001_{2}$:

$1 \times 2^4 + 1 \times 2^3 + 0 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 16 + 8 + 0 + 0 + 1 = 25_{10}$

## Pierwsze 17 Potęg Liczby 2

1. $2^0 = 1$
2. $2^1 = 2$
3. $2^2 = 4$
4. $2^3 = 8$
5. $2^4 = 16$
6. $2^5 = 32$
7. $2^6 = 64$
8. $2^7 = 128$
9. $2^8 = 256$
10. $2^9 = 512$
11. $2^{10} = 1024$
12. $2^{11} = 2048$
13. $2^{12} = 4096$
14. $2^{13} = 8192$
15. $2^{14} = 16384$
16. $2^{15} = 32768$
17. $2^{16} = 65536$
