string= """

I have provided this text to provide tips on creating interesting paragraphs.

First, start with a clear topic sentence that introduces the main idea.

Then, support the topic sentence with specific details, examples, and evidence.

Vary the sentence length and structure to keep the reader engaged.

Finally, end with a strong concluding sentence that summarizes the main points.

Remember, practice makes perfect!

"""
no_mark_string=''
for i in string:
    if i.isalpha() or i.isspace():
        no_mark_string+=i
lst=no_mark_string.split()
word_lst=[]
for word in lst:
    if word not in word_lst:
        word_lst.append(word)
print(len(word_lst))

