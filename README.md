# Algorithm-for-breaking-passwords
Anthony Romo UIDE
El algoritmo se ejecuta abriendo el archivo .py en este caso bruteforce.py en nuestro IDE de confianza.
Luego se procede a cambiar en la última línea de código bruteforce("abc"), por la contraseña que queramos probar por ejemplo bruteforce("newcont")
Ejemplos de salida:

<img width="337" height="52" alt="image" src="https://github.com/user-attachments/assets/0ca27090-a3ac-48e4-8a95-a1c0b1bbcffa" />

<img width="329" height="51" alt="image" src="https://github.com/user-attachments/assets/4b766905-5251-425f-9ebb-14d885718c42" />

<img width="314" height="55" alt="image" src="https://github.com/user-attachments/assets/d2180ac5-97ef-4d09-8e7b-7765aee43d55" />

¿Qué pasa si la contraseña tiene 8+ caracteres y usa mayúsculas, números y símbolos?
Se lleva al límite el crecimiento exponencial que tiene el algoritmo, haciendo que el objetivo buscado tarde una gran suma de tiempo no razonable, siendo que una contraseña de 8 caracteres tiene 85⁸ ≈ 2.7 * 10¹⁵ combinaciones. Esto contando que use mayúsculas, números y símbolos.
