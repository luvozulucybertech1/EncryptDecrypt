# EncryptDecrypt

## Background
Zlatan and Lionel have been best friends since birth. The two of them are completely inseparable, and even when they’re apart, they’re constantly staring at their phones sending messages
to each other. Lionel occasionally gets annoyed with Zlatan who often sends a few too many
Christiano Ronaldo memes. Apart from that, though, things couldn’t be better.
One day however, Zlatan stumbled upon a whole bunch of conspiracy websites. The sites
managed to convince him that not only is the earth flat, but that it’s actually a good idea for a
man to have both a ponytail and a goatee! But worst of all, Zlatan became totally convinced
that NASA1 are spying on his conversations with Lionel.
Lionel knows that this is completely ridiculous, but he’s too busy making adverts for Lays
chips, and doesn’t really have the time to argue with Zlatan — he reckons that it’s just easier to
go along with Zlatan’s delusions. He does want to make Zlatan feel better though, so he gets in
touch with you and asks if you could make some program that could encrypt and decrypt their
conversations and ensure that no-one is able to read any intercepted messages.
You’d rather not help out — you’ve got many matrices that need to be Gaussian eliminated —
but then you remember that Lionel doesn’t pay tax, and so probably has lots of money. He might
even give you some! You can’t get in touch with him, so you leave a note with his receptionist
(some Brazilian with ridiculous hair called Neymar) saying that you’ll take the job.
# The Plan
Even though you’ve offered to help out, you’re still very busy and so you can’t allocate too much
time to this task. Implementing a robust encryption system would take too long, so you decide
to provide security through obfuscation. This means that if the people spying on you don’t know how you’ve altered a message, they probably won’t be able to recover the original message.
Here’s the method you come up with:
First, Zlatan and Lionel both agree on a certain secret number b ∈ [2, 36]. Let’s assume
Zlatan wants to send a message to Lionel. Each character in the string is converted into its ASCII
representation. Next, each ASCII number is converted from its decimal representation to base-b.
These numbers (which are now in base-b) are sent to Lionel. Lionel receives these numbers and
converts them back to base-10 numbers. These numbers are converted back to the characters
they represent in ASCII, and the original message can then read. A graphical representation of
the process is drawn below.

![image](https://github.com/luvozulucybertech1/EncryptDecrypt/assets/160118100/65b1f1a8-3ef8-41b2-a936-5d95685cf0ce)

You’re not going to write this as one big system, so you break it down into a series of tasks.


## 1. The First Task

Write a program that reads in a line of text and converts each character into its ASCII representation. The line of text may contain letters, digits, punctuation and spaces. Your output should
consist of a single line containing each character’s ASCII number. Numbers should be separated
by a single space space.

### 1.1
Input consists of a single line of text (there may be spaces, so be careful). You can assume that
the line is never empty.

### 1.2 Output
Your output should consist of a single line of integers, separated by spaces. Each integer is the
ASCII representation of the characters of the given string.

## 2. The Second Task

Your next task is to do the opposite of the first task: write a program that accepts a number of
integers, converts them to their ASCII characters, and outputs the resulting string.
### 2.1 Input
The input consists of a series of integers, one per line. You can assume that there will always
be at least one number given. The end of the input will be signalled by the number −1, which
simply tells you when to stop reading in, and should not be processed.
### 2.2 Output
Your output should consist of a single line of text that results when the given integers are converted into characters.

## 3. The Third Task 
Your next task is write a program that converts decimal integers into a given base.
### 3.1 Input
The first line of input is a number 2 ≤ b ≤ 36, which represents the base we want to convert to.
The rest of the input consists of a series of non-negative integers, one per line. You can assume
that there will always be at least one number given. The end of the input will be signalled by
the number −1, which simply tells you when to stop reading in, and should not be processed.
### 3.2 Output
For each decimal number, output its base-b representation. Use the capital letters for bases
greater than 10.

## 4. The Fourth Task 
Now, write a program that does the opposite of the previous task: converts integers in a given
base into decimal numbers.
### 4.1 Input
The first line of input is a number 2 ≤ b ≤ 36, which represents the base we want to convert
from. The rest of the input consists of a series of strings, one per line. Be aware that these
cannot be treated simply as integers, because they may contain letters. If there are letters, they
are always uppercase. You can assume that there will always be at least one number given. The
end of the input will be signalled by −1, which simply tells you when to stop reading in, and
should not be processed.
### 4.2 Output
For each base-b number, output its decimal representation.

## 5. The Fifth Task 
It’s finally time to put everything together! The input format will be slightly different here, but
essentially you’ll be combining the previous tasks to make a full system that is able to encrypt or
decrypt any message.
### 5.1 Input
Input consists of three lines. The first line is a string that has either the value encrypt or decrypt
and represents the mode. The next line contains a single integer 2 ≤ b ≤ 36 which represents
the base you’ll be working with. The third line is the message (which is either a normal text
message, or a series of base-b numbers separated by spaces, depending on the mode). You can
assume the third line is never empty.
### 5.2 Output
Your output will be a single line that depends on the mode.
### 5.2.1 Encryption Mode
If the mode is encrypt, then the message line is a normal message that needs to be encrypted.
Convert each character to its ASCII value, and then convert each of those numbers to their baseb representations. Output these base-b numbers on a single line, with each number separated by
a single space.
### 5.2.2 Decryption Mode
If the mode is decrypt, then the message line is a series of base-b numbers, each separated by a
single space. The message line does not end with a −1. Convert each number into its decimal
representation, and then into its ASCII character. Output all of these characters on a single line.
### 5.3 Some Advice
Reading in a series of strings on a single line is not a trivial task. You will need to look up how
to split a line into its individual entries.

## 6. The Sixth Task 
This task requires you to extend the previous task slightly in order to handle a message that
might be a paragraph.
### 6.1 Input
Input consists of at least 3 lines. The first line is a string that has either the value encrypt
or decrypt and represents the mode. The next line contains a single integer 2 ≤ b ≤ 36 which
represents the base you’ll be working with. The remaining lines are the message (either a normal
text message, or a series of base-b numbers separated by spaces, depending on the mode). You
can assume that there is at least one message line.
### 6.2 Output
Your output will be a single line that depends on the mode.
### 6.2.1 Encryption Mode
If the mode is encrypt, then the message lines represent a normal message that needs to be
encrypted. Convert each character to its ASCII value (newlines should also be converted to their
ASCII value), and then convert each of those numbers to their base-b representations. Output
these base-b numbers on a single line, with each number separated by a single space.
### 6.2.2 Decryption Mode
If the mode is decrypt, then the message line is a single line consisting of any amount of base-b
numbers, each separated by a single space. The message line does not end with a −1. Convert
each number into its decimal representation, and then into its ASCII character. Output all of
these characters. Because some of these numbers may be the newline character, your output
may appear on multiple lines.

### Sources
Dr Steven James - github.com/sd-james
                - linkedin.com/in/steven-james
