import React from 'react';
import { Field, useFormikContext } from 'formik';
import Select from 'react-select';

// Custom Select Component
const CustomSelectComponent = ({
  className,
  placeholder,
  field,
  form,
  options,
  isMulti = false,
  ...props
}) => {
  const onChange = (option) => {
    form.setFieldValue(
      field.name,
      isMulti
        ? option.map((item) => item.value)
        : option.value
    );
  };

  const getValue = () => {
    if (options) {
      // Ensure field.value is an array and not null or undefined
      const fieldValue = Array.isArray(field.value) ? field.value : [];
  
      return isMulti
        ? options.filter(option => fieldValue.includes(option.value))
        : options.find(option => option.value === field.value);
    } else {
      return isMulti ? [] : "";
    }
  };

  return (
    <Select
      className={className}
      name={field.name}
      value={getValue()}
      onChange={onChange}
      placeholder={placeholder}
      options={options}
      isMulti={isMulti}
      {...props}
    />
  );
};

// Formik Field Wrapper for Custom Select
const CustomSelect = (props) => (
  <Field component={CustomSelectComponent} {...props} />
);

export default CustomSelect;