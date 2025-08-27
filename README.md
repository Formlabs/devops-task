Technology choices and possible alternatives:

- **Docker**: I  used it because it allows me to package the application and all its dependencies into a portable image, ensuring it runs consistently across any environment.

Alternatives: Podman and Buildah offer similar functionality and can even be lighter since they do not require a running daemon. However, Docker remains the industry standard and is widely supported by CI/CD tools and cloud providers.

- **k3s**: I used k3s as my Kubernetes distribution because it’s a lightweight alternative to Minikube. It provides a full Kubernetes API while consuming fewer resources and booting up much faster, which is ideal for local development and fast CI testing.

- **Ansible**: Ansible is used to automate deployment and infrastructure tasks in a simple way where it's human-readable and idempotent also worth to note that it's Agentless (Doesn't require extra software) and works really well with both Docker and Kubernetes. 

Alternatives: Chef and Puppet but they use Ruby for (Chef) and DSLs for (Puppet) which is harder to read and write than Ansible.

- **GitHub Actions**: I used it since it integrates directly with the repository that i have on Github and doesn't need to install or configure external CI/CD servers. Since Actions trigger automatically on Push events.

Alternatives: Jenkins and GitLab CI; I haven't used Jenkins since it requires maintaining my own Jenkins server, plugins and agents. 
As for GitLab CI, it's relaly strong especially for GitLab hosted projects, but I didn't need to use it here since my repo is available on GitHub.
