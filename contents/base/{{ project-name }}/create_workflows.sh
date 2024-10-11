WORKFLOWS_DIR=$1
if [ -z "$WORKFLOWS_DIR" ]; then
  WORKFLOWS_DIR=/app/src/{{ project_name }}/metaflows
  echo "Assuming $WORKFLOWS_DIR for WORKFLOWS_DIR"
fi

export METAFLOW_DATASTORE_SYSROOT_S3=s3://metaflow-dev-us-west-2-p6m-dev
for FILE in $WORKFLOWS_DIR/*; do python3 $FILE --datastore=s3 argo-workflows create; done