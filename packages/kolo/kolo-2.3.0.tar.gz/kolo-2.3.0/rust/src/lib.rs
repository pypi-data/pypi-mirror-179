#[cfg(not(PyPy))]
use pyo3::exceptions::PyTypeError;
#[cfg(not(PyPy))]
use pyo3::ffi;
#[cfg(not(PyPy))]
use pyo3::prelude::*;

#[cfg(not(PyPy))]
extern "C" fn profile(
    _obj: *mut ffi::PyObject,
    _frame: *mut ffi::PyFrameObject,
    what: i32,
    _arg: *mut ffi::PyObject,
) -> i32 {
    let event = {
        if what == ffi::PyTrace_CALL {
            "call"
        } else if what == ffi::PyTrace_RETURN {
            "return"
        } else {
            return 0;
        }
    };
    let _frame = _frame as *mut ffi::PyObject;
    Python::with_gil(|py| unsafe {
        let obj = PyObject::from_borrowed_ptr_or_err(py, _obj);
        let frame = PyObject::from_borrowed_ptr_or_opt(py, _frame);
        let arg = PyObject::from_borrowed_ptr_or_opt(py, _arg);
        let args = (frame, event, arg);
        match obj {
            Ok(obj) => match obj.call1(py, args) {
                Ok(_) => 0,
                Err(err) => {
                    err.restore(py);
                    -1
                }
            },
            Err(err) => {
                err.restore(py);
                -1
            }
        }
    })
}

#[cfg(not(PyPy))]
#[pyfunction]
fn register_profiler(profiler: PyObject) -> Result<(), PyErr> {
    Python::with_gil(|py| {
        if profiler.as_ref(py).is_callable() {
            unsafe {
                ffi::PyEval_SetProfile(Some(profile), profiler.into_ptr());
            }
            Ok(())
        } else {
            Err(PyTypeError::new_err("profiler object is not callable"))
        }
    })
}

#[cfg(not(PyPy))]
#[pymodule]
fn _kolo(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(register_profiler, m)?)?;
    Ok(())
}
