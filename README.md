## Objectives
- Documenting down my self learning project on how to deploy AWS CloudFormation Stack using Github Action

## Article
- I also wrote an [article](https://aws.plainenglish.io/how-i-deploy-aws-cloudformation-stack-using-github-action-7f3e8a46fdfa) to share about the learning details of this project

# DevOps Baseline

Desplegar el template template-baseline-devops.yaml en las cuentas de despliegue (ej. Dev, QA, Prod).

Los parametros que debe respetar el despliegue son los siguientes:

ArtifactsBucketArn: (vacio)
CloudFormationExecutionRoleArn: (vacio)
CreateImageRepository: false
CreateNewOidcProvider: false
IdentityProviderThumbprint: (vacio)
ImageRepositoryArn: (vacio)
OidcClientId: (vacio)
OidcProviderUrl: (vacio)
PipelineExecutionRoleArn: (vacio)
PipelineUserArn: (vacio)
SubjectClaim: (vacio)
UseOidcProvider: false