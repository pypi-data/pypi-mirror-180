
use pyo3::prelude::*;
use comportlist::available_ports;
/// Formats the sum of two numbers as string.
#[pyfunction]
fn list_ports(keyserck:Vec<&str>) -> PyResult<Vec<Vec<String>>> {
    let mut r_data = Vec::new();
    for idx in available_ports(keyserck){
        let mut tmp = Vec::new();
        match idx.serial_number {
            Some(item) =>tmp.push(item),
            None =>tmp.push("".to_string())
        }
        match idx.product{
            Some(item) =>tmp.push(item),
            None =>tmp.push("".to_string())
        }
        match idx.manufacturer{
            Some(item) =>tmp.push(item),
            None =>tmp.push("".to_string())
        }
        r_data.push(tmp);
    }
    Ok(r_data)
}

/// A Python module implemented in Rust.
#[pymodule]
fn comportlist(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(list_ports, m)?)?;
    Ok(())
}