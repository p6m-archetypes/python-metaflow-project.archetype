WORKFLOWS_DIR=$1
if [ -z "$WORKFLOWS_DIR" ]; then
  WORKFLOWS_DIR=/app/src/{{ project_name }}/metaflows
  echo "Assuming $WORKFLOWS_DIR for WORKFLOWS_DIR"
fi

for FILE in $WORKFLOWS_DIR/*; do python3 $FILE --datastore=s3 argo-workflows create; done