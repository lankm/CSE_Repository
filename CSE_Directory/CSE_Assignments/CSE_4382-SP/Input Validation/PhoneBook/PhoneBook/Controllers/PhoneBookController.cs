using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PhoneBook.Exceptions;
using PhoneBook.Model;
using PhoneBook.Services;

namespace PhoneBook.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class PhoneBookController : ControllerBase
    {
        private readonly IPhoneBookService _phoneBookService;
        private readonly ILogger<PhoneBookController> _logger;

        public PhoneBookController(IPhoneBookService phoneBookService, ILogger<PhoneBookController> logger)
        {
            _phoneBookService = phoneBookService;
            _logger = logger;
        }

        [HttpGet]
        [Route("list")]
        public IEnumerable<PhoneBookEntry> List()
        {
            _logger.LogInformation(" ");
            return _phoneBookService.List();
        }

        [HttpPost]
        [Route("add")]
        public IActionResult Add([FromBody]PhoneBookEntry newEntry)
        {
            string logString = string.Format("\"{0}\",\"{1}\"", newEntry.Name, newEntry.PhoneNumber); ;
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            try
            {
                _phoneBookService.Add(newEntry);

                _logger.LogInformation(logString);
                return Ok();
            }
            catch (ArgumentException ex)
            {
                _logger.LogWarning(logString);
                return BadRequest(ex.Message);
            }
        }

        [HttpPut]
        [Route("deleteByName")]
        public IActionResult DeleteByName([FromQuery] string name)
        {
            string logString = String.Format("\"{0}\"", name);
            try
            {
                _phoneBookService.DeleteByName(name);

                _logger.LogInformation(logString);
                return Ok();
            }
            catch (ArgumentException ex)
            {
                _logger.LogWarning(logString);
                return BadRequest(ex.Message);
            }
            catch (NotFoundException ex)
            {
                return NotFound(ex.Message);
            }

        }

        [HttpPut]
        [Route("deleteByNumber")]
        public IActionResult DeleteByNumber([FromQuery] string number)
        {
            string logString = String.Format("\"{0}\"", number);
            try
            {
                _phoneBookService.DeleteByNumber(number);

                _logger.LogInformation(logString);
                return Ok();
            }
            catch (ArgumentException ex)
            {
                _logger.LogWarning(logString);
                return BadRequest(ex.Message);
            }
            catch (NotFoundException ex)
            {
                return NotFound(ex.Message);
            }
        }

        [HttpPut]
        [Route("deleteAll")]
        public IActionResult DeleteAll()
        {
            _phoneBookService.DeleteAll();
            _logger.LogInformation(" ");
            return Ok();
        }
    }
}