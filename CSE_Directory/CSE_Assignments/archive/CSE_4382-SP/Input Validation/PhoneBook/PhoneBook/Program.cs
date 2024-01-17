// I wish I understood what all this means. I only understand what I've added.

using Microsoft.AspNetCore.Server.Kestrel.Core;
using Microsoft.EntityFrameworkCore;
using Microsoft.OpenApi.Models;
using PhoneBook.Data;
using PhoneBook.Services;

namespace PhoneBook
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            //logging setup
            builder.Host.ConfigureLogging(logging =>
            {
                logging.ClearProviders();
                logging.AddLog4Net();   // pulls log4net.config
                logging.AddConsole();
            });
            
            // Add services to the container.
            builder.Services.AddControllers();

            //sqlite setup
            builder.Services.AddDbContext<DataContext>(options =>
            {
                options.UseSqlite(builder.Configuration.GetConnectionString("WebApiDatabase"));
            });

            // Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
            builder.Services.AddEndpointsApiExplorer(); // adds PhoneBookController.cs as the interface
            builder.Services.AddSwaggerGen(options =>
            {
                options.SwaggerDoc("v1", new OpenApiInfo
                {
                    Version = "v1",
                    Title = "PhoneBook API",
                    Description = "A simple API for managing a phone book."
                });
            });
            builder.Services.AddScoped<IPhoneBookService, DictionaryPhoneBookService>();


            var app = builder.Build();
            // Configure the HTTP request pipeline.
            if (app.Environment.IsDevelopment())
            {
                app.UseSwagger();
                app.UseSwaggerUI();
            }
            app.UseHttpsRedirection();
            app.UseAuthorization();
            app.MapControllers();

            app.Run();
        }
    }
}