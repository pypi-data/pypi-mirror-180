use std::cell::RefCell;

use cpython::{py_module_initializer, py_class, PyResult, PyErr, exc, PyNone};

py_class!(class Auth |py| {
    data inner: RefCell<core::Auth>;
    def __new__(_cls, postgres_url: String, redis_url: String) -> PyResult<Auth> {
        tokio::runtime::Runtime::new()
            .unwrap()
            .block_on(async {
                Auth::create_instance(py,
                    RefCell::new(core::init_auth(postgres_url, redis_url)
                        .await
                        .or(Err(PyErr::new::<exc::ValueError, _>(py, "Error initializing auth")))?)
                )
            })
    }
    def get_token_expire_time(&self) -> PyResult<usize> {
        Ok(match self.inner(py).borrow().token_expire_time {
            Some(x) => x,
            None => 0,
        })
    }
    def set_token_expire_time(&self, time: usize) -> PyResult<PyNone> {
        self.inner(py).borrow_mut().token_expire_time = Some(time);
        Ok(PyNone)
    }
    def login(&self, email: String, password: String) -> PyResult<String> {
        tokio::runtime::Runtime::new()
            .unwrap()
            .block_on(async {
                core::login(&mut self.inner(py).borrow_mut(), email, password)
                    .await
                    .or(Err(PyErr::new::<exc::ValueError, _>(py, "Error logging in")))
            })
    }
    def logout(&self, token: String) -> PyResult<PyNone>{
        core::logout(&mut self.inner(py).borrow_mut(), token)
            .or(Err(PyErr::new::<exc::ValueError, _>(py, "Error logging out")))?;
        Ok(PyNone)
    }
    def register(&self, email: String, password: String) -> PyResult<PyNone> {
        match tokio::runtime::Runtime::new()
            .unwrap()
            .block_on(async {
                core::create_user(&mut self.inner(py).borrow_mut(), email, password)
                    .await
                    .or(Err(PyErr::new::<exc::ValueError, _>(py, "Error registering")))
            })
        {
            Ok(_) => Ok(PyNone),
            Err(e) => Err(e),
        }
    }
    def update_user(&self, token: String, email: String, password: String, logout: bool) -> PyResult<PyNone> {
        let email = if email == "" { None } else { Some(email) };
        let password = if password == "" { None } else { Some(password) };
        match tokio::runtime::Runtime::new()
            .unwrap()
            .block_on(async {
                core::update_user(&mut self.inner(py).borrow_mut(), token, email, password, logout)
                    .await
                    .or(Err(PyErr::new::<exc::ValueError, _>(py, "Error updating user")))
            })
        {
            Ok(_) => Ok(PyNone),
            Err(e) => Err(e),
        }
    }
    def admin_update_user(&self, token: String, email: String, password: String, logout: bool) -> PyResult<PyNone> {
        let email = if email == "" { None } else { Some(email) };
        let password = if password == "" { None } else { Some(password) };
        match tokio::runtime::Runtime::new()
            .unwrap()
            .block_on(async {
                core::admin_update_user(&mut self.inner(py).borrow_mut(), token, email, password, logout)
                    .await
                    .or(Err(PyErr::new::<exc::ValueError, _>(py, "Error updating user")))
            })
        {
            Ok(_) => Ok(PyNone),
            Err(e) => Err(e),
        }
    }
    def delete_user(&self, token: String) -> PyResult<PyNone> {
        match tokio::runtime::Runtime::new()
            .unwrap()
            .block_on(async {
                core::delete_user(&mut self.inner(py).borrow_mut(), token)
                    .await
                    .or(Err(PyErr::new::<exc::ValueError, _>(py, "Error deleting user")))
            })
        {
            Ok(_) => Ok(PyNone),
            Err(e) => Err(e),
        }
    }
    def admin_delete_user(&self, token: String) -> PyResult<PyNone> {
        match tokio::runtime::Runtime::new()
            .unwrap()
            .block_on(async {
                core::admin_delete_user(&mut self.inner(py).borrow_mut(), token)
                    .await
                    .or(Err(PyErr::new::<exc::ValueError, _>(py, "Error deleting user")))
            })
        {
            Ok(_) => Ok(PyNone),
            Err(e) => Err(e),
        }
    }
    def verify_token(&self, token: String) -> PyResult<String> {
        match tokio::runtime::Runtime::new()
            .unwrap()
            .block_on(async {
                core::verify_token(&mut self.inner(py).borrow_mut(), token)
                    .await
                    .or(Err(PyErr::new::<exc::ValueError, _>(py, "Error verifying token")))
            })
        {
            Ok(x) => Ok(x),
            Err(e) => Err(e),
        }
    }

});

py_module_initializer!(passtoken, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(py, "Auth", py.get_type::<Auth>())?;
    Ok(())
});