import pycms.gfmhandle
import SiteHTML.SiteHTML
import os.path
import glob


def add_html_to_template(new_html, new_title):
    html_str = """<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>"""
    html_str += new_title
    html_str += """</title>
    <!-- Begin Global Head Content -->
    <!-- End Global Head Content -->
</head>
<body>
<!-- Begin Global header -->
<!-- End Global header -->
"""
    html_str += new_html
    html_str += """
<!-- Begin Global footer -->
<!-- End Global footer -->
</body>
</html>
"""
    return html_str


def run_me(fdir):
    glob_pat = glob.glob(os.path.join(fdir, '*.md'))
    for fp in glob_pat:
        gfmh1 = pycms.gfmhandle.GfmHandle()
        gfmh1.input = fp
        bfn = os.path.basename(fp).rpartition('.')[0]
        gfmh1.login = pycms.gfmhandle.Login(username='iJunkie22', password='walru1995github')
        result1 = gfmh1.main()
        result2 = add_html_to_template(result1, bfn)

        with open(os.path.join(fdir, bfn + '.html'), 'w', encoding='utf-8') as fd2:
            fd2.write(result2)
            fd2.truncate()

    fp2 = os.path.abspath(fdir)
    SiteHTML.SiteHTML.run([fp2])


run_me('./sample_site/JS_Project/')


