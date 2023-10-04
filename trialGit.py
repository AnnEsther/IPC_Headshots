import git

dir = "/Users/annjo/Git/Headshots/IPC_Headshots"

repo = git.Repo()  # ex. "/User/some_user/some_dir"
origin = repo.remote("origin")  
assert origin.exists()
origin.fetch()

new_branch = repo.create_head("main", origin.refs.main)  # replace prod with master/ main/ whatever you named your main branch
new_branch.checkout()

f = open("demofile.txt", "w")
f.write("some demofile content")
f.close()

repo.git.add('--all')
#repo.index.add(dir+"/demofile.txt")  # in this case filename would be "/User/some_user/some_dir/demofile.txt"
repo.index.commit("your commit message")
...  # more commits here if needed

repo.git.push("--set-upstream", origin, repo.head.ref)