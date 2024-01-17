using Microsoft.Data.Sqlite;
using Microsoft.EntityFrameworkCore;
using PhoneBook.Data;
using PhoneBook.Exceptions;
using PhoneBook.Model;
using System.Xml.Linq;

namespace PhoneBook.Services
{
    public class DictionaryPhoneBookService : IPhoneBookService
    {
        public DbContext _db;
        public DictionaryPhoneBookService(DataContext database)
        {
            database.Database.Migrate();
            _db = database;
        }

        // IPhoneBookService functions
        public IEnumerable<PhoneBookEntry> List()
        {
            return _db.Set<PhoneBookEntry>();
        }
        public void Add(PhoneBookEntry phoneBookEntry)
        {
            if (phoneBookEntry.Name == null || phoneBookEntry.PhoneNumber == null) {
                throw new ArgumentException("Name and phone number must both be specified.");}

            //input validation
            bool invalidName = !ValidationService.ValidName(phoneBookEntry.Name);
            bool invalidNum = !ValidationService.ValidNumber(phoneBookEntry.PhoneNumber);
            if (invalidName && invalidNum) {
                throw new ArgumentException(ValidationService._nameErr + " and " + ValidationService._numberErr);}
            else if (invalidName) {
                throw new ArgumentException(ValidationService._nameErr);}
            else if (invalidNum) {
                throw new ArgumentException(ValidationService._numberErr);}

            // adding value to database
            _db.Add(phoneBookEntry);
            try {
                _db.SaveChanges();
            } catch(DbUpdateException) {
                throw new ArgumentException($"An entry with the name \"{phoneBookEntry.Name}\" already exists.");}
        }
        public void DeleteByName(string name)
        {
            //input validation
            bool invalidName = !ValidationService.ValidName(name);
            if (invalidName) {
                throw new ArgumentException(ValidationService._nameErr);}

            // locate entry
            var entry = _db.Set<PhoneBookEntry>().Find(name);
            if (entry == null)
            {
                throw new NotFoundException($"No phonebook entry found containing name \"{name}\".");
            }

            // save
            _db.Remove(entry);
            _db.SaveChanges();
        }
        public void DeleteByNumber(string number)
        {
            // input validation
            bool invalidNumber = !ValidationService.ValidNumber(number);
            if (invalidNumber) {
                throw new ArgumentException(ValidationService._numberErr);}
            
            // locate entry
            PhoneBookEntry? entry = null;
            foreach( PhoneBookEntry pbe in _db.Set<PhoneBookEntry>())
            {
                if (pbe.PhoneNumber == null)
                    throw new ArgumentNullException("No Phone number");
                if(pbe.PhoneNumber.Equals(number))
                {
                    entry = pbe;
                    break;
                }
            }
            if (entry == null)
            {
                throw new NotFoundException($"No phonebook entry found containing name \"{number}\".");
            }

            // save changes
            _db.Remove(entry);
            _db.SaveChanges();
        }
        public void DeleteAll()
        {
            _db.RemoveRange(_db.Set<PhoneBookEntry>());
            _db.SaveChanges();
        }
    }
}
