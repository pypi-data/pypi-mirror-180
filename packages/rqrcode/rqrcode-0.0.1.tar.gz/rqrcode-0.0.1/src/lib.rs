use fast_qr::convert::{image::ImageBuilder, svg::SvgBuilder, Builder, Shape};
use fast_qr::qr::QRBuilder;
use pyo3::prelude::*;

/// 二维码png图片生成函数
#[pyfunction]
fn qrcode_img(data: String, save_path: String) {
    let qrcode = QRBuilder::new(data.into()).build().unwrap();

    let _img = ImageBuilder::default()
        .shape(Shape::RoundedSquare)
        .fit_width(600)
        .to_file(&qrcode, &save_path);
}

/// 二维码svg图片生成函数
#[pyfunction]
fn qrcode_svg(data: String, save_path: String) {
    let qrcode = QRBuilder::new(data.into()).build().unwrap();

    let _svg = SvgBuilder::default()
        .shape(Shape::RoundedSquare)
        .to_file(&qrcode, &save_path);
}

/// 二维码unicode生成函数
#[pyfunction]
fn qrcode_unicode(data: String) {
    let qrcode = QRBuilder::new(data.into()).build().unwrap();

    let str = qrcode.to_str();
    println!("{}", str);
}

/// A Python module implemented in Rust.
#[pymodule]
fn rqrcode(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(qrcode_img, m)?)?;
    m.add_function(wrap_pyfunction!(qrcode_svg, m)?)?;
    m.add_function(wrap_pyfunction!(qrcode_unicode, m)?)?;
    Ok(())
}
