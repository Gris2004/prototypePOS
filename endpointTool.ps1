#function to use curl in a endpoint with the get method
function Fetch-Data{
    param([string]$uri)
    $result = & curl.exe -s $uri
    return $result
}
