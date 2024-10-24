import { useState, useEffect } from "react";
import { useTheme } from "../Context/ThemeContext";
import { useNavigate } from "react-router-dom"; // Import useNavigate
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash, faBox } from "@fortawesome/free-solid-svg-icons"; // Import Trash and Box icons
import { Link } from "react-router-dom";
import axios from 'axios';
const Services = () => {
  const { isDarkTheme } = useTheme();
  const [servicesData, setServicesData] = useState([]);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate(); // Initialize useNavigate
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen(prevState => !prevState);
};

useEffect(() => {
  const fetchServices = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:5000/services");
      setServicesData(response.data);
    } catch (error) {
      setError(error.response ? error.response.data : 'Error fetching services');
    } finally {
      setIsLoading(false);
    }
  };

  fetchServices();
}, []);

  if (isLoading) {
    return <div className="text-center mt-4">Loading...</div>;
  }

  if (error) {
    return <div className="text-red-500 text-center mt-4">Error: {error}</div>;
  }
  
  const length = Object.keys(servicesData).length;
  return (
    <div>
      <div class="flex justify-between items-center">
        <Link
          to="/services"
          className="text-gray-600 text-3xl font-bold hover:text-gray-900"
        >
          Services
        </Link>

        <div class="flex flex-col mt-2 items-center mr-4">
          <span class="text-xs xs:text-sm text-gray-900 mb-1">
            Showing {length} Services
          </span>
          <div className="flex mt-2 gap-1">
            <button class="text-sm bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded-l">
              Prev
            </button>
            <button class="text-sm bg-gray-300 hover:bg-gray-400 text-gray-800 font-semibold py-2 px-4 rounded-r">
              Next
            </button>
          </div>
        </div>
      </div>
      <div class="shadow-md sm:rounded-lg">
        <div class="p-4">
          <label for="table-search" class="sr-only">
            Search
          </label>
          <div class="relative mt-1">
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg
                class="w-5 h-5 text-gray-500 dark:text-gray-400"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                  clip-rule="evenodd"
                ></path>
              </svg>
            </div>
            <input
              type="text"
              id="table-search"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-80 pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="What are you looking for?"
            />
          </div>
        </div>
        <div className="overflow-x-auto overflow-y-auto">
        <table class=" min-w-full  border border-gray-300 text-sm text-left text-gray-500 dark:text-gray-400">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" class="px-6 py-3 text-base">
                Name of the Service
              </th>
              <th scope="col" class="px-6 py-3 text-base">
                ID
              </th>
              
              <th scope="col" class="px-6 py-3 text-base">
                Desired State
              </th>
              <th scope="col" class="px-6 py-3 text-base">
                Image Name
              </th>
              <th scope="col" class="px-6 py-3 text-base">
                Port Number
              </th>
              <th scope="col" class="px-6 py-3 text-base">
                Replicas
              </th>
              <th scope="col" className="px-6 py-3 text-base">
                        <p className="ml=1">State:</p>
                        <select aria-label="select border-none">
                            <option class="text-sm ">None</option>
                            <option class="text-sm text-green-800">Running</option>
                            <option class="text-sm text-red-800">Stopped</option>
                        </select>
                    
              </th>
              <th scope="col" class="px-6 py-3 text-base">
                Status
              </th>
              <th scope="col" class="px-6 py-3 text-base"></th>
              <th scope="col" class="px-6 py-3 text-base"></th>
              <th scope="col" class="px-6 py-3 text-base">
                Creation Time
              </th>
            </tr>
          </thead>
          <tbody>
          {servicesData.map((data) => (
  <tr
    className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-200"
    key={data.ID}
  >
    <td
      scope="row"
      className="px-6 py-4 font-medium text-gray-900 dark:text-white whitespace-nowrap"
    >
      {data.Spec?.Name ?? "Null"}
    </td>
    <td
      scope="row"
      className="px-6 py-4 font-medium text-gray-900 dark:text-white whitespace-nowrap"
    >
      {data.ID ?? "Null"}
    </td>
    
    <td
      scope="row"
      className="px-6 py-4 font-medium text-gray-900 dark:text-white whitespace-nowrap"
    >
      {(data.Endpoint?.Ports?.[0]?.PublishMode + " " + data.Endpoint?.Ports?.[0]?.Protocol) ?? "Null"}
    </td>
    <td
  scope="row"
  className="truncate px-6 py-4 font-medium text-gray-900 dark:text-white"
>
  {(() => {
    const image = data.Spec?.TaskTemplate?.ContainerSpec?.Image ?? "Null";
    const regex = /^(.*?)@/;
    const match = image.match(regex);
    return match ? match[1] : image; // Return the part before '@ or the original string if no '@' is found
  })()}
</td>
    <td
      scope="row"
      className="px-6 py-4 font-medium text-gray-900 dark:text-white whitespace-nowrap"
    >
      {(data.Endpoint?.Ports?.[0]?.PublishedPort + ":" + data.Endpoint?.Ports?.[0]?.TargetPort)?? "Null"}
    </td>
    <td
      scope="row"
      className="px-6 py-4 font-medium text-gray-900 dark:text-white whitespace-nowrap text-center"
    >
      {data.Spec?.Mode?.Replicated?.Replicas ?? "Null"}
    </td>
    <td
      scope="row"
      className={`px-6 py-4 font-medium ${
        data.Spec?.TaskTemplate?.Runtime === "Running" ? "text-green-600" : "text-red-900"
      } dark:text-white whitespace-nowrap`}
    >
      {data.Spec?.TaskTemplate?.Runtime ?? "Null"}
    </td>
    <td
      scope="row"
      className="px-6 py-4 font-medium text-gray-900 dark:text-white whitespace-nowrap"
    >
      {data.Version?.Index ?? "Null"}
    </td>
    <td className="px-6 py-4 text-right">
      <Link
        to="/services/edit"
        className="font-medium text-blue-600 dark:text-blue-500 hover:underline"
      >
        Edit
      </Link>
    </td>
    <td className="row px-6 py-4">
      <button className="flex items-center justify-center text-red-600 hover:text-red-800">
        <FontAwesomeIcon icon={faTrash} className="mr-2" />
      </button>
    </td>
    <td
      scope="row"
      className="px-6 py-4 font-medium text-gray-900 dark:text-white whitespace-nowrap"
    >
      {data.CreatedAt ?? "Null"}
    </td>
  </tr>
))}
          </tbody>
        </table>
        </div>
      </div>
    </div>
  );
};

export default Services;
