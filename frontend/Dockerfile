# Frontend Dockerfile - Modo Desarrollo
FROM node:20-slim

WORKDIR /app

# Copiar archivos de dependencias
COPY package*.json ./
RUN npm install

# Copiar el resto del código
COPY . .

# Exponer el puerto por defecto de Vite
EXPOSE 5173

# Comando para iniciar el modo desarrollo
# --host es necesario para que Docker pueda mapear el puerto
CMD ["npm", "run", "dev", "--", "--host"]
