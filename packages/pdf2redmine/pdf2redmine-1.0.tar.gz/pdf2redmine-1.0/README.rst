
pdf2redmine
===============
A software tool to automatically read a pdf docuument for annotations (comments)
and upload those to a redmine server using a personal API access token

Installing
============

.. code-block:: bash

    pip install pdf2redmine

Usage
=====

.. code-block:: python

    from pdf2redmine import read_and_upload
    redmine_url = '<your-redmine-server-url>'
    redmine_key = '<your-redmine-api-access-key>'
    redmine_project_id = '<your-remine-project-id>'
    file_link = '<some-link-to-the-local-file-for-online-access>'
    file_path = 'C:/temp/dummy_document_with_comments.pdf'
    ids = read_and_upload(file_path, redmine_url, redmine_key, redmine_project_id, link=file_link)
    print('Generated the following issues:')
    print(ids)



