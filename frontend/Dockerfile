# Frontend Dockerfile - Etapa de Build
FROM node:20-slim AS build

WORKDIR /app

# Argumento de build para la URL de la API
ARG VITE_API_URL=/api
ENV VITE_API_URL=$VITE_API_URL

# Copiar archivos de dependencias e instalar
COPY package*.json ./
RUN npm install

# Copiar el resto del código y construir
COPY . .
RUN npm run build

# Etapa de Producción con Nginx
FROM nginx:stable-alpine

# Copiar la configuración personalizada de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copiar los archivos construidos desde la etapa anterior
COPY --from=build /app/dist /usr/share/nginx/html

# Exponer el puerto 80 (puerto interno del contenedor)
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
