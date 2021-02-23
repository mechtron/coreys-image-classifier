{{- define "releaseLabels" }}
app: {{ .Chart.Name | trunc 63 }}
version: {{ .Chart.Version }}
release: {{ .Release.Name }}
{{- end }}

{{- define "name" -}}
{{- .Release.Name | trunc 63 -}}
{{- end -}}

{{- define "apiName" -}}
{{- printf "%s-%s" .Release.Name "api" | trunc 63 -}}
{{- end -}}

{{- define "cacheName" -}}
{{- printf "%s-redis-master" .Release.Name | trunc 63 -}}
{{- end -}}

{{- define "dbName" -}}
{{- printf "%s-%s" .Release.Name "mysql" | trunc 63 -}}
{{- end -}}

{{- define "webName" -}}
{{- printf "%s-%s" .Release.Name "web" | trunc 63 -}}
{{- end -}}
