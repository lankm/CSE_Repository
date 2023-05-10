docker load -i "%cd%/phonebookimg.tar"
docker run -dt -v "%cd%:/root/.microsoft/usersecrets:ro" -v "%cd%:/root/.aspnet/https:ro" -e "ASPNETCORE_ENVIRONMENT=Development" -e "ASPNETCORE_URLS=https://+:443;http://+:80" -P --name PhoneBook --entrypoint tail phonebook -f /dev/null
docker exec -d PhoneBook dotnet PhoneBook.dll


