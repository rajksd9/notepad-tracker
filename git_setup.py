import git
import os
import sys




def check_git(repo_path):
    if not os.path.exists(repo_path):
        print(f"Error: The path {repo_path} does not exist.")
        sys.exit(1)

    try:
        repo = git.Repo(repo_path)
        print(f"Repository found at {repo_path}.")
    except:
        print(f"No Git repository found at {repo_path}.")
        repo = git.Repo.init(repo_path)
        print(f"Initialized new Git repository at {repo_path}.")
    
    return repo

def commit_changes(repo, commit_message,remote_url):
    if repo.is_dirty() or len(repo.untracked_files)>0:
        print("Changes detected. Committing...")
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        
        if not repo.remotes:
            repo.create_remote("origin",remote_url)
        origin = repo.remotes.origin
        try:
            origin.push()
            print('Changes committed and pushed successfully.')
        except :
            print(f"Push failed.")
            print("Setting upstream branch and retrying push...")
            current_branch = repo.active_branch.name
            repo.git.push('--set-upstream', 'origin', current_branch)
    else:
        print('No changes to commit.')

    
