import git

repo = git.Repo()  # ex. "/User/some_user/some_dir"
origin = repo.remote("origin")  

def connect():
    assert origin.exists()
    origin.fetch()

    new_branch = repo.create_head("main", origin.refs.main)  # replace prod with master/ main/ whatever you named your main branch
    new_branch.checkout()

def update(id):
    repo.git.add('--all')
    repo.index.commit("Generated IPC " +str(id)+" LINK : https://github.com/AnnEsther/IPC_Headshots/blob/main/Output/"+str(id)+".png")

    repo.git.push("--set-upstream", origin, repo.head.ref)