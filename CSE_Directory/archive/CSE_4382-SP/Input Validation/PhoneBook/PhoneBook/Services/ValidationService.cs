// change it so it doesn't depend on being static to be a service. not important though.
// also change to act through an interface

using System.Text.RegularExpressions;

namespace PhoneBook.Services
{
    public class ValidationService
    {
        // class variable
        internal const string _nameErr = "invalid name";
        private const string _nameRegex = "(([a-zA-Z]+['’])*[a-zA-Z]+)"; //unit for a part of a name
        private static readonly string[] _namePatterns = new string[]{
            "^RGX([ \\-]RGX)?[ \\-]RGX$", // first middle? last
            "^RGX, RGX([ \\-]RGX.?)?$",   // last, first middle
            "^RGX$"};                     // name
        internal const string _numberErr = "invalid phone number";
        private const string _countryRegex = "(\\+|(011 )|(00 ))?";
        private static readonly string[] _numberPatterns = new string[]{
            "^\\d{5}([ .]\\d{5})?$", //internal organization... or 10 digit
            "^(CRX45[ .])?(\\d{2}[ .]){3}\\d{2}$", //AA AA AA AA Danish
            "^(CRX45[ .])?\\d{4}[ .]\\d$", //AAAA AAAA Danish
            "^(CRX[1-9]\\d{0,2}[ .-]?)?"+"(\\(?[1-9]\\d{1,2}\\)?[ .-]?)?"+"\\d{3}[ .-]\\d{4}$"};    // catch-all

        // interface functions
        internal static bool ValidName(string name)
        {
            RegexOptions options = RegexOptions.None;
            foreach (string pattern in _namePatterns)
            {
                string newPattern = pattern.Replace("RGX", _nameRegex);
                if (Regex.IsMatch(name, newPattern, options))
                {
                    return true;
                }
            }
            return false;
        }
        internal static bool ValidNumber(string number)
        {
            RegexOptions options = RegexOptions.None;
            foreach (string pattern in _numberPatterns)
            {
                string newPattern = pattern.Replace("CRX", _countryRegex);
                if (Regex.IsMatch(number, newPattern, options))
                {
                    return true;
                }
            }
            return false;
        }

    }
}
