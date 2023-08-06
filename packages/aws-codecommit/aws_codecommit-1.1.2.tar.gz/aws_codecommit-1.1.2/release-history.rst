.. _release_history:

Release and Version History
==============================================================================


Backlog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


1.1.2 (2022-12-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- fix a bug that ``get_commit`` didn't load the commit message into ``Commit`` object.


1.1.1 (2022-12-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add ``aws_codecommit.better_boto`` module, a objective oriented boto3.client("codecommit") API. I am actively adding more feature to it.
- add ``aws_codecommit.console`` module, a aws codecommit console url builder.


1.0.1 (2022-12-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First API stable release
- add the following API:
    - ``aws_codecommit.CodeCommitEvent``
    - ``aws_codecommit.SemanticBranchEnum``
    - ``aws_codecommit.is_certain_semantic_branch``
    - ``aws_codecommit.SemanticCommitEnum``
    - ``aws_codecommit.is_certain_semantic_commit``
    - ``aws_codecommit.ConventionalCommitParser``
    - ``aws_codecommit.default_parser``


0.0.7 (2022-08-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add ``conventional_commits`` parser module, but not used in the CI bot lambda handler.


0.0.6 (2022-07-26)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add ``is_pr_from_specific_branch_to_specific_branch`` method.
- add ``get_commit_message_and_committer`` function.


0.0.5 (2022-07-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add a few condition test functions
- Add aws account id, and aws region attribute to data model


0.0.4 (2022-07-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add AWS CodeCommit notification event data model
