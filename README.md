## Guía para despliege de solución con Github Actions
Para desplegar una solución de AWS SAM, se deben seguir los siguientes pasos:

1. Desplegar los recursos necesarios en las cuentas de ambientes (ej. Dev, QA, Prod).
2. Agregar los archivos necesarios a la solución SAM.
3. Agregar secretos en el repositorio de Github.
4. Agregar los parámetros del stack por ambiente

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

(Repetir esto por cada ambiente, en este ejemplo asumiremos solo DEV y el prefijo de todos los secretos serán DEV_) Dentro del repositorio en Settings > Secrets and variables > Actions > Secretes, en el apartado de Repository secretes, agregar los siguientes secretos:


- DEV_ACCESS_KEY: El Access Key del usuario programatico a utilizar (Para ambiente de Dev).
- DEV_SECRET_KEY: El Secret Key del usuario programatico a utilizar (Para ambiente de Dev).
- DEV_PIPELINE_EXECUTION_ROLE: Agregar el Output con nombre 'PipelineExecutionRole' del stack desplegado en el Paso 1 para el entorno de Dev.
- DEV_CLOUDFORMATION_EXECUTION_ROLE: Agregar el Output con nombre 'CloudFormationExecutionRole' del stack desplegado en el Paso 1 para el entorno de Dev.
- DEV_ARTIFACTS_BUCKET: Agregar el Output con nombre 'ArtifactsBucketName' del stack desplegado en el Paso 1 para el entorno de Dev.

# (Paso 4) Agregar los parámetros del stack por ambiente.

(Repetir esto por cada ambiente, en este ejemplo asumiremos solo DEV y el prefijo de la variable será DEV_) Dentro del repositorio en Settings > Secrets and variables > Actions > Variables, en el apartado de Repository variables, agregar la siguiente variable:

- DEV_PARAMETERS: (Para ambiente de Dev) agregar en formato json los parametros utilizados en el stack de sam, este debe llevar la siguiente estructura:
[{"ParameterKey": "Parameter1", "ParameterValue": "el-valor-del-parameter1"}, {"ParameterKey": "Parameter2", "ParameterValue": "el-valor-del-parameter2"}]