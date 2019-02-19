{{- define "classifier.release_labels" }}
app: {{ printf "%s" .Release.Name | trunc 63 }}
version: {{ .Chart.Version }}
release: {{ .Release.Name }}
{{- end }}

{{- define "classifier.full_name" -}}
{{- printf "%s" .Release.Name | trunc 63 -}}
{{- end -}}
