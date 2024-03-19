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
