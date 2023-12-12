# Simulare-fp-212

## Robot Activities

Scrieți un program pentru gestionarea activității unor roboți. Vor fi suportate următoarele operații:

1. **Afişarea tuturor activităților:** Afișați activitățile care conțin în descriere un șir de caractere citit de la tastatură, ordonate descrescător după nivelul de baterie. Afișați un mesaj specific dacă nu există nicio astfel de activitate. (0.5p)

2. **Robotul pe grid 2D:** Robotul se mișcă pe un grid 2D cartezian, urmărind instrucțiunile din activitate. Fiecare instrucțiune de mișcare scade nivelul de baterie cu 10%. Acțiunea halt încarcă bateria cu 5%. Se citește o poziție de start <x, y>. Pentru fiecare activitate, afișați poziția finală și nivelul final de baterie după urmărirea instrucțiunilor. Activitatea se termină când se termină instrucțiunile sau nu mai este baterie pentru a continua. (3p)

Activitățile se citesc dintr-un fișier cu formatul de mai jos. Instrucțiunile posibile sunt up, down, right, left, halt. Introduceți minim 10 intrări în fișier.

```plaintext
<id>;<nivel_baterie>;<descriere>;<instr1,instr2,instr3,...>
1;36;find Nemo;up,right,down,halt,right
2;33;go on adventure;up,up, down, halt, right, right, up
3;65;explore territory; right, down, down, down, left, halt
```
## Cerințe:

**La cerința 1:** Pentru șirul "re" veți afișa activitățile cu id-urile 2 și 3...

**La cerința 2:** Având poziția de start (3,2), veți afișa:

1: `<5,2>, 1`  
2: `<3,3>, 8`  
3: `<3,-1>, 20`

## Punctaje:

- 1p oficiu
- 1p arhitectura, proporțional cu funcționalitățile implementate corect.
- 2p stil, specificații și teste, proporțional cu funcționalitățile implementate.

## Observații:

- Nu se acceptă aplicații care nu folosesc clase/obiecte.
- Dacă datele nu sunt citite/scrise din fișier, se înjumătățește punctajul la fiecare funcționalitate.
- Nu se pot folosi proiecte existente (trebuie pornit de la 0) fără ajutor exterior.

## Punctaj obținut pe:

| 1   | 1.5 | 2   | 2.5 | 3   | 3.5 | 4   | 4.5 | 5   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **funcționalități**                    | 1   | 1.3 | 1.6 | 2   | 2.4 | 2.8 | 3.2 | 3.6 |
| **stil, specificații, teste, arhitectura** | 3   | 3.8 | 4.6 | 5.5 | 6.4 | 7.3 | 8.2 | 9.1 |

## Nota finală maximă: 10
