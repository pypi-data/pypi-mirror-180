# -*- coding: utf-8 -*-

"""
Better codecommit boto3 client
"""

from typing import Optional, Tuple
from .boto_ses import cc_client


def get_commit_message_and_committer(
    repo_name: str,
    commit_id: str,
) -> Tuple[str, str]:  # pragma: no cover
    """
    Get a specific commit message for a commit.

    :param repo_name: CodeCommit repository name
    :param commit_id: sha1 of commit id
    """
    res = cc_client.get_commit(
        repositoryName=repo_name,
        commitId=commit_id,
    )
    commit_message = res["commit"]["message"].split("\n")[0]
    committer_name = res["commit"]["committer"]["name"]
    return commit_message, committer_name


def get_last_commit_id_of_branch(
    repo_name: str,
    branch_name: str,
) -> str:  # pragma: no cover
    """
    See function name.

    :param repo_name: CodeCommit repository name
    :param branch_name: git branch name
    :return: last commit id of branch
    """
    res = cc_client.get_branch(
        repositoryName=repo_name,
        branchName=branch_name,
    )
    return res["branch"]["commitId"]


def commit_file(
    repo_name: str,
    branch_name: str,
    file_content: bytes,
    file_path: str,
    commit_message: str,
    author_name: str,
    author_email: str,
    skip_if_no_change: bool = True,
) -> Optional[str]:  # pragma: no cover
    """
    Wrapper around boto3 CodeCommit client ``put_file`` method.

    Log some info and handle error.

    :return: the commit id of this action, could return None if failed
    """
    last_commit_id = get_last_commit_id_of_branch(repo_name, branch_name)
    try:
        res = cc_client.put_file(
            repositoryName=repo_name,
            branchName=branch_name,
            fileContent=file_content,
            filePath=file_path,
            fileMode="NORMAL",
            parentCommitId=last_commit_id,
            commitMessage=commit_message,
            name=author_name,
            email=author_email,
        )
        commit_id = res["commitId"]
        return commit_id
    except Exception as e:
        if skip_if_no_change:
            # file not changed skip commit
            if "SameFileContentException" in e.__class__.__name__:
                return None
        raise e


def get_text_file_content(
    repo_name: str,
    commit_id: str,
    file_path: str,
) -> str:
    """
    Get text file content from CodeCommit repo.
    """
    res = cc_client.get_file(
        repositoryName=repo_name,
        commitSpecifier=commit_id,
        filePath=file_path,
    )
    return res["fileContent"].decode("utf-8")


def post_comment_for_pull_request(
    repo_name: str,
    pr_id: str,
    before_commit_id: str,
    after_commit_id: str,
    content: str,
) -> str:
    """
    Put a comment in CodeCommit Pull Request activity view.
    """
    res = cc_client.post_comment_for_pull_request(
        pullRequestId=pr_id,
        repositoryName=repo_name,
        beforeCommitId=before_commit_id,
        afterCommitId=after_commit_id,
        content=content,
    )
    return res["comment"]["commentId"]


def update_comment(
    comment_id: str,
    content: str
):  # pragma: no cover
    """
    Update an existing comment.
    """
    cc_client.update_comment(
        commentId=comment_id,
        content=content,
    )


def reply_comment(
    comment_id: str,
    content: str,
) -> str:  # pragma: no cover
    """
    Reply to comment
    """
    res = cc_client.post_comment_reply(
        inReplyTo=comment_id,
        content=content,
    )
    return res["comment"]["commentId"]
