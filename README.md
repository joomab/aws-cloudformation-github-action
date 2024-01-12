## Guía para despliege de solución con Github Actions
Para desplegar una solución de AWS SAM, se deben seguir los siguientes pasos:

1. Desplegar los recursos necesarios en las cuentas de ambientes (ej. Dev, QA, Prod).
2. Agregar los archivos necesarios a la solución SAM.
3. Agregar secretos en el repositorio de Github.

A continuación el detalle del proceso de los pasos anteriores.

# (Paso 1) Desplegar los recursos necesarios en las cuentas de ambientes (ej. Dev, QA, Prod).

Desplegar el template template-baseline-devops.yaml en las cuentas de despliegue (ej. Dev, QA, Prod).

Los parametros que debe respetar el despliegue son los siguientes:

- ArtifactsBucketArn: (vacio)
- CloudFormationExecutionRoleArn: (vacio)
- CreateImageRepository: false
- CreateNewOidcProvider: false
- IdentityProviderThumbprint: (vacio)
- ImageRepositoryArn: (vacio)
- OidcClientId: (vacio)
- OidcProviderUrl: (vacio)
- PipelineExecutionRoleArn: (vacio)
- PipelineUserArn: (vacio)
- SubjectClaim: (vacio)
- UseOidcProvider: false

Nota: En la fase de creación del stack, en la sección de "Tags", agregar los tags que correspondan. Esta seccion asegura que todos los recursos desplegados en el stack se creen con esos tags.

# (Paso 2) Desplegar los recursos necesarios en las cuentas de ambientes (ej. Dev, QA, Prod).

Dentro de la carpeta sam-app agregar la solución SAM completa que desea desplegar.

# (Paso 3) Agregar secretos en el repositorio de Github.

Dentro del repositorio 