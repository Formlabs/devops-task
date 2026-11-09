This repo serves as the client app example.
The main infra/ci functionality lives in [awslab](https://github.com/veygawslab/awslab)

I did not particularly keep it simple. But I definitely needed some baseline infra to get off the ground.

Rather than building the cicd into the app itself; I created the cicd mechanisms alongside the infra itself in the awslab repo. The git commit messages may be useful, but this description is a better collection of my strategies/implementations here:

The awslab repo provisions the network, cluster, argo, etc.

The infra components (for now) are managed via TF/helm and the "apps" are hosted "on argo" and deployed via GHA/kargo using a gitops approach. Alternatively (and ideally) you could host all helm charts on argo (load balancer controller, argo itself, etc) but there's a chicken/egg issue with that. It's resolvable but I didn't take it that far.

I chose EKS because that's what I'm most familiar with, and there are nice terraform modules for provisioning eks clusters.

The awslab repo provisions stuff from a local terragrunt stack. This is not what I would do for a prod architecture; but for this demo it's sufficient. Ultimately the terraform applies would ideally be behind ci (Atlantis or otherwise). You could also use crossplane instead and apply/promote infra in the same way as product apps. Something I did in my last role, but thought that was a bit much here.

I also set up my own GHA runners because I'm a fan of hosting your own runners. I stuck with GHA because that definitely seemed like it would cause the least barriers. I've used gitlab and dagger (within Jenkins) as well, but I didn't want to fumble with integration for this.

I set up a domain and LB, because I did end up setting up ingresses/certs for the helloapp. I chose traefik because it's a pleasant tool to configure. I chose an NLB/traefik combo versus an aws managed ALB, as I like to configure as much stuff in k8s as I can, vs aws managed resources. That's not something I always strive for, but it's definitely a preference. Reason being, the more stuff that's in k8s, the more I can leverage shared functionality (observability, etc), versus having to juggle something like cloudwatch AND Prometheus, for example.

I used ecr for hosting images/charts. I would normally prefer something like artifactory/nexus on k8s versus ECR (reasons stated previously), but ecr was just easier to set up for this.

Argo/kargo: I quite like gitops in general. I believe in IaC, and gitops is an extension of that belief system. Argocd is something I'm quite familiar with; which is why I chose it over others. Flux doesn't really have a UI as well.

I recently got introduced to kargo. This is absolutely the best way to manage promotions in argocd. Previously I was writing gitlab jobs for manually working with argo applications. Kargo is much better and more powerful, hence I chose that.

Users open up pull requests which triggers build/test/etc. You can then deploy that image to a dev environment via kargo. Merges to main trigger a release and subsequent build. Users then deploy to prd via kargo as well. Releases to prd are gated by an actual git tag, which comes from merges to main. I use calver over direct semver because it's just easier and you don't have to have arguments about what "type of release" this may be. If a user doesn't particularly care about your app version (like for example a package dependency) then calver is something I prefer.

Argo is hosted at [argo.veyga.click](https://argo.veyga.click)
Kargo is hosted at [kargo.veyga.click](https://kargo.veyga.click)
Currently only I have access to those, but read-only perms can be granted on request.
Git interactions trigger new resource in kargo (i.e. 'Freight') and interactions
via Kargo 'promote' freight to the appropriate env.

This is a relatively straight forward Kargo setup; see the main [project](https://github.com/akuity/kargo)

I also created microservice and kargo charts. These are used by client apps. I'd rather avoid devs writing helm charts themselves, and instead opting into options provided by charts. This is why the helloapp itself is pretty minimal: the ci functionality is provided elsewhere.

You can see the live dev/prd envs:

https://helloapp-dev.veyga.click

https://helloapp.veyga.click

What's 'not done' that I would do in a more robust prod system:
- tf for provisioning/managing git repos
- split dev/prod gitops repos and protect prod more
- more git repo protections
- aws organizations
- separate accounts/clusters/networking
- vpn/non-public argo/kargo etc
- host infra helm charts in argo versus in terraform
    - there's a chicken/egg thing for certain charts
    - would need to bring all charts in argo itself now that argo is up
    - right now it's just hosting product-y apps
- run TF applies via CI, not locally
    - the local 'just' commands are easier for this takehome
- store secrets (github PATs etc) in an actual store
    - utilize them in CI runs
- more granular argo appprojects
- SSO logins
- run artifactory/nexus over ecr
- bubble calver version up to prod
- image/tag cleanup as cronjob
- ephemeral dev envs
    - the current 'dev' is really more of a shared staging env
