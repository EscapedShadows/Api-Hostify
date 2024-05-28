SOME FILES ARE NOT THERE YET BE PATIENT!

# API Hostify

A project by EscapedShadows for **everyone** for **Free**.

---

API Hostify is an open-source project maintained by EscapedShadows, licensed under the Apache 2.0 License.

API Hostify allows anyone to quickly turn any Python-supporting device into a simple JSON API.

There are three versions of API Hostify:

- Bucket
- Bin
- Container

Each version has its pros and cons.

Let's go through the versions and see what the differences are!

## Bucket

As you might have already guessed, Bucket utilizes a common way of storing mass JSON data (a bit modified): with something called "Buckets."

You can imagine it like having a folder with many files named Bucket01.json, Bucket02.json, etc.

It's easy to avoid getting messy with this system but can be difficult to remember where specific data is stored.

## Bin

Basically a bigger version of Bucket that utilizes the original system of Bucket data storage.

Instead of just having files, each bucket is another folder, which means you can create as many files in one bucket as you want.

This can lead to some confusion and difficulty finding data (working on a system to export all data in the near future).

## Container

Whoever uses this either has a small project or hates themselves.

Container is not a bigger version of Bin but rather a mass storage consisting of **one** single JSON file storing **all** of the data.

## As you might have already seen in the repository, there are six Python files in total:

- bucketWIN.py
- binWIN.py
- containerWIN.py
- bucketUNIX.py
- binUNIX.py
- containerUNIX.py

There are different versions for Windows and Linux. Although it would work with one file on both platforms, each version has bug patches specific to the OS so it runs at optimal performance.

## So why did I create this project?

Because I know what a pain it is to write a simple and clean API, making it work, bug fixing and then the system implementations, writing the documentation, maintaining the project and just cause I like free stuff lmao.