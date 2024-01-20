using PhoneBook.Model;

namespace PhoneBook.Services
{
    public interface IPhoneBookService
    {
        IEnumerable<PhoneBookEntry> List();
        void Add(PhoneBookEntry phoneBookEntry);
        void DeleteByName(string name);
        void DeleteByNumber(string number);
        void DeleteAll();
    }
}