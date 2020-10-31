cd ~/blog_html


bash latex.sh
bash gen_index.sh
git add *
git commit -m "update"
git push blog master # Init: git remote add blog https://github.com/huhaoo/huhaoo.github.io.git
