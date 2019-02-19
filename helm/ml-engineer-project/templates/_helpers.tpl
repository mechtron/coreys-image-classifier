{{- define "ml-engineer-project.release_labels" }}
app: {{ printf "%s-%s" .Chart.Name .Release.Name | trunc 63 }}
version: {{ .Chart.Version }}
release: {{ .Release.Name }}
{{- end }}

{{- define "ml-engineer-project.full_name" -}}
{{- printf "%s-%s" .Chart.Name .Release.Name | trunc 63 -}}
{{- end -}}
