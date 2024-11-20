# Enc2024-Cryptography: Imagica  (WINNER FOR 'BEST CRYPTOGRAPHY FOR SOCIETY'!)
Cryptographic Python tool using images to encrypt data.

This tool will provide a simple, yet highly flexible way to provide secure encryption.
The main idea behind this encryption tool is to allow the user to freely use something meaningful to keep their data secure; And what else can hold more meaning to you than a lovely image!

The way this tool functions is pretty simple: Using the RGB data of the image to produce encrypted ciphertext from basic, unprotected strings of data.
An encryption algorithm makes use of the image 'fed' by the user to gather said RGB data, pretty much allowing a unique cipher for each image! How cool is that!

As shown in the demo, the encryption algorithm has different stages:
* 1st is the hashing stage, where the data from the user interacts directly with the key (image) provided.
* 2nd is the shuffling stage, where the now-hashed-data is then shifted to the right, to again add a feeling of randomness and disguising any potential patterns.

An unencryption algorithm is also provided, which only works if you provide the same exact image, due to the nature of XOR operations.

The entire project runs on a Flask local-web server, which allows the user to interact with the program without the usage of the terminal; With a frontend built with only CSS and HTML.
The user is free to both decrypt and encrypt, using whichever image they want; And they can return to the main page even after recieving the result.

This, honestly, simple piece of code however has amazing potential dependant on where it is used/deployed.
With constant real-time image-stream, this will allow for infinite & unique encrypted results, making each piece of data unique from the last and most importantly: Uniquely secure.
Furthermore, its' simplicity is a clear statement to how such idea can not only be easily used, even by those who do not know nor want to understand the true importance of encryption, but it can also be easily replicated; Only requiring furhter imagination.

Imagica is a tool that rides on a new prespective on encryption:
Where prespectives are what truly is infinite.


# HOW TO USE:
1* Enter your piece of data that you'd like to encrypt.

2* Enter a png, jpeg, your grandma even! Any image you'd like!

3* Choose between the encrypt/decrypt modes.

4* Press the confirm button and VOILA! Your piece of data is encrypted successfully! Use the same image to decrypt later if you want.

