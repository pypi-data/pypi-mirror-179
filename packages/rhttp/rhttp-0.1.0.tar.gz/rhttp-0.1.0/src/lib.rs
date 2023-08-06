use pyo3::prelude::*;
use pyo3::Python;
mod request;


#[pyclass]
pub struct Response {
    #[pyo3(get)]
    status: u16,
    #[pyo3(get)]
    body: String,
}

#[pyfunction]
fn get() -> Response {
    
    Response {
        status: 200,
        body: "".to_string(),
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn rhttp(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get, m)?)?;
    Ok(())
}