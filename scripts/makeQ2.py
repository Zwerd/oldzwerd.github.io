from shutil import copyfile
import shutil

shutil.copy('../_posts/2018-04-22-javascript-tutorial.md', './jsPost.md')
jsOldPost = open('./jsPost.md','r')
count = len(jsOldPost.readlines())
jsOldPost.close()


jsNewPost = open('./jsNewPost.md', 'w')
jsOldPost = open('./jsPost.md', 'r')
for i in range(count):
    jsNewPost.write(jsOldPost.readline())
    if i == count -4:



